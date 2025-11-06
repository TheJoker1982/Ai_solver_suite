const crypto = require('crypto');

/**
 * Drive Verification Agent
 * Double-checks the Google Drive import to ensure ALL files were imported
 * No file left behind - every screenshot, solver, tool matters!
 */
class DriveVerificationAgent {
    constructor(pool, driveService) {
        this.pool = pool;
        this.driveService = driveService;
        this.verificationLog = [];
        this.missingFiles = [];
        this.duplicateFiles = [];
        this.importedFiles = new Set();
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const logEntry = { timestamp, type, message };
        this.verificationLog.push(logEntry);
        
        console.log(`[VERIFICATION ${type.toUpperCase()}] ${message}`);
        
        // Store in database
        this.pool.query(
            `INSERT INTO ai_learning_log (timestamp, log_type, message, created_at)
             VALUES ($1, $2, $3, NOW())`,
            [timestamp, `verification_${type}`, message]
        ).catch(err => console.error('Error logging:', err));
    }

    async loadImportedFiles() {
        try {
            const result = await this.pool.query(
                `SELECT sha256_hash, filename, drive_file_id, file_size
                 FROM imported_assets`
            );

            for (const row of result.rows) {
                this.importedFiles.add(row.sha256_hash);
            }

            this.log(`Loaded ${this.importedFiles.size} imported files from database`);
            return this.importedFiles.size;

        } catch (error) {
            this.log(`Error loading imported files: ${error.message}`, 'error');
            return 0;
        }
    }

    async scanDriveRecursively(folderId = 'root', path = '/', depth = 0) {
        try {
            if (depth > 20) {
                this.log(`Max depth reached at ${path}`, 'warn');
                return { files: 0, folders: 0 };
            }

            let filesCount = 0;
            let foldersCount = 0;
            let pageToken = null;

            do {
                const response = await this.driveService.files.list({
                    q: `'${folderId}' in parents and trashed = false`,
                    fields: 'nextPageToken, files(id, name, mimeType, size, md5Checksum, modifiedTime)',
                    pageSize: 100,
                    pageToken: pageToken
                });

                const files = response.data.files || [];

                for (const file of files) {
                    if (file.mimeType === 'application/vnd.google-apps.folder') {
                        foldersCount++;
                        this.log(`📁 Scanning folder: ${path}${file.name}/`);
                        
                        const subResults = await this.scanDriveRecursively(
                            file.id, 
                            `${path}${file.name}/`, 
                            depth + 1
                        );
                        
                        filesCount += subResults.files;
                        foldersCount += subResults.folders;
                    } else {
                        filesCount++;
                        await this.verifyFile(file, path);
                    }
                }

                pageToken = response.data.nextPageToken;
            } while (pageToken);

            return { files: filesCount, folders: foldersCount };

        } catch (error) {
            this.log(`Error scanning ${path}: ${error.message}`, 'error');
            return { files: 0, folders: 0 };
        }
    }

    async verifyFile(file, path) {
        try {
            // Check if file was imported
            const result = await this.pool.query(
                `SELECT id, sha256_hash, file_size 
                 FROM imported_assets 
                 WHERE drive_file_id = $1 OR filename = $2`,
                [file.id, file.name]
            );

            if (result.rows.length === 0) {
                // File NOT imported!
                this.log(`❌ MISSING: ${path}${file.name} (${this.formatBytes(file.size)})`, 'error');
                this.missingFiles.push({
                    driveId: file.id,
                    filename: file.name,
                    path: path,
                    size: file.size,
                    modifiedTime: file.modifiedTime
                });
            } else if (result.rows.length > 1) {
                // Duplicate import
                this.log(`⚠️ DUPLICATE: ${file.name} (imported ${result.rows.length} times)`, 'warn');
                this.duplicateFiles.push({
                    filename: file.name,
                    count: result.rows.length,
                    ids: result.rows.map(r => r.id)
                });
            } else {
                // File imported correctly
                this.log(`✅ Verified: ${file.name}`, 'success');
            }

        } catch (error) {
            this.log(`Error verifying ${file.name}: ${error.message}`, 'error');
        }
    }

    formatBytes(bytes) {
        if (!bytes) return '0 B';
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
    }

    async runFullVerification() {
        try {
            this.log('═══════════════════════════════════════════════════════════');
            this.log('🔍 STARTING DRIVE VERIFICATION - DOUBLE-CHECKING IMPORT');
            this.log('═══════════════════════════════════════════════════════════');

            // Step 1: Load all imported files
            const importedCount = await this.loadImportedFiles();

            // Step 2: Scan entire Drive
            this.log('📂 Scanning Google Drive (all folders, up to 20 levels deep)...');
            const scanResults = await this.scanDriveRecursively();

            // Step 3: Generate report
            this.log('═══════════════════════════════════════════════════════════');
            this.log('📊 VERIFICATION REPORT');
            this.log('═══════════════════════════════════════════════════════════');
            this.log(`Total Drive Files Found: ${scanResults.files}`);
            this.log(`Total Drive Folders: ${scanResults.folders}`);
            this.log(`Files in Database: ${importedCount}`);
            this.log(`Missing Files: ${this.missingFiles.length}`);
            this.log(`Duplicate Files: ${this.duplicateFiles.length}`);
            
            if (this.missingFiles.length > 0) {
                this.log('');
                this.log('❌ MISSING FILES THAT NEED IMPORT:', 'error');
                for (const file of this.missingFiles.slice(0, 20)) {
                    this.log(`   - ${file.path}${file.filename} (${this.formatBytes(file.size)})`, 'error');
                }
                if (this.missingFiles.length > 20) {
                    this.log(`   ... and ${this.missingFiles.length - 20} more`, 'error');
                }
            }

            if (this.duplicateFiles.length > 0) {
                this.log('');
                this.log('⚠️ DUPLICATE FILES:', 'warn');
                for (const dup of this.duplicateFiles.slice(0, 10)) {
                    this.log(`   - ${dup.filename} (imported ${dup.count} times)`, 'warn');
                }
            }

            // Step 4: Store verification results
            await this.storeVerificationResults(scanResults);

            this.log('═══════════════════════════════════════════════════════════');
            if (this.missingFiles.length === 0) {
                this.log('✅ VERIFICATION COMPLETE - ALL FILES IMPORTED!', 'success');
            } else {
                this.log(`⚠️ VERIFICATION COMPLETE - ${this.missingFiles.length} FILES NEED IMPORT`, 'warn');
            }
            this.log('═══════════════════════════════════════════════════════════');

            return {
                success: true,
                totalDriveFiles: scanResults.files,
                importedFiles: importedCount,
                missingFiles: this.missingFiles,
                duplicateFiles: this.duplicateFiles,
                completeness: ((importedCount / scanResults.files) * 100).toFixed(2) + '%'
            };

        } catch (error) {
            this.log(`Verification failed: ${error.message}`, 'error');
            return {
                success: false,
                error: error.message
            };
        }
    }

    async storeVerificationResults(scanResults) {
        try {
            await this.pool.query(
                `INSERT INTO drive_verification_runs 
                 (total_drive_files, total_imported_files, missing_count, duplicate_count, 
                  missing_files, duplicate_files, completed_at)
                 VALUES ($1, $2, $3, $4, $5, $6, NOW())`,
                [
                    scanResults.files,
                    this.importedFiles.size,
                    this.missingFiles.length,
                    this.duplicateFiles.length,
                    JSON.stringify(this.missingFiles),
                    JSON.stringify(this.duplicateFiles)
                ]
            );

            this.log('Verification results saved to database');

        } catch (error) {
            // Table might not exist - create it
            await this.pool.query(`
                CREATE TABLE IF NOT EXISTS drive_verification_runs (
                    id SERIAL PRIMARY KEY,
                    total_drive_files INTEGER,
                    total_imported_files INTEGER,
                    missing_count INTEGER,
                    duplicate_count INTEGER,
                    missing_files JSONB,
                    duplicate_files JSONB,
                    completed_at TIMESTAMP DEFAULT NOW()
                )
            `);

            // Retry
            await this.storeVerificationResults(scanResults);
        }
    }

    getStatus() {
        return {
            verificationLog: this.verificationLog.slice(-50),
            missingFiles: this.missingFiles,
            duplicateFiles: this.duplicateFiles,
            importedCount: this.importedFiles.size
        };
    }
}

module.exports = DriveVerificationAgent;
