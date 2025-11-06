const crypto = require('crypto');

/**
 * AUTO-COPY ALL DRIVE FILES
 * Simple approach: Copy EVERYTHING from Drive to database
 * User deletes duplicates/junk later (way easier than manual import)
 */
class AutoCopyAllDriveFiles {
    constructor(pool, driveService) {
        this.pool = pool;
        this.driveService = driveService;
        this.totalCopied = 0;
        this.errors = [];
        this.log = [];
    }

    logMessage(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const entry = { timestamp, type, message };
        this.log.push(entry);
        console.log(`[AUTO-COPY ${type.toUpperCase()}] ${message}`);
    }

    async copyEverythingFromDrive(folderId = 'root', path = '/', depth = 0) {
        try {
            if (depth > 25) {
                this.logMessage(`Max depth reached at ${path}`, 'warn');
                return;
            }

            this.logMessage(`📂 Scanning: ${path}`);
            
            let pageToken = null;
            
            do {
                const response = await this.driveService.files.list({
                    q: `'${folderId}' in parents and trashed = false`,
                    fields: 'nextPageToken, files(id, name, mimeType, size, md5Checksum, modifiedTime, webViewLink)',
                    pageSize: 100,
                    pageToken: pageToken,
                    supportsAllDrives: true,
                    includeItemsFromAllDrives: true
                });

                const files = response.data.files || [];
                
                for (const file of files) {
                    if (file.mimeType === 'application/vnd.google-apps.folder') {
                        // Recurse into folder
                        await this.copyEverythingFromDrive(
                            file.id, 
                            `${path}${file.name}/`, 
                            depth + 1
                        );
                    } else {
                        // Copy file to database
                        await this.copyFileToDatabase(file, path);
                    }
                }

                pageToken = response.data.nextPageToken;
            } while (pageToken);

        } catch (error) {
            this.logMessage(`Error scanning ${path}: ${error.message}`, 'error');
            this.errors.push({ path, error: error.message });
        }
    }

    async copyFileToDatabase(file, path) {
        try {
            // Check if already copied
            const existing = await this.pool.query(
                'SELECT id FROM imported_assets WHERE drive_file_id = $1',
                [file.id]
            );

            if (existing.rows.length > 0) {
                this.logMessage(`⏭️ Skip (already copied): ${file.name}`, 'info');
                return;
            }

            // CRITICAL: ZIPs are loaded with important data - MUST download
            const isArchive = file.name.toLowerCase().endsWith('.zip') || 
                            file.name.toLowerCase().endsWith('.rar') || 
                            file.name.toLowerCase().endsWith('.7z') ||
                            file.mimeType === 'application/zip' ||
                            file.mimeType === 'application/x-zip-compressed';
            
            if (isArchive) {
                this.logMessage(`📦 ARCHIVE (critical data): ${path}${file.name} (${this.formatBytes(file.size)})`, 'success');
            } else {
                this.logMessage(`📥 Copying: ${path}${file.name} (${this.formatBytes(file.size)})`);
            }

            // Download file data
            let fileData = null;
            let mimeType = file.mimeType;

            // Skip Google Workspace files (Docs, Sheets, etc.) - can't download as binary
            if (file.mimeType.startsWith('application/vnd.google-apps.')) {
                this.logMessage(`⏭️ Skip (Google Workspace file): ${file.name}`, 'warn');
                return;
            }

            // Download file content
            try {
                const response = await this.driveService.files.get(
                    { fileId: file.id, alt: 'media' },
                    { responseType: 'arraybuffer' }
                );
                fileData = Buffer.from(response.data);
            } catch (downloadError) {
                this.logMessage(`⚠️ Download failed for ${file.name}: ${downloadError.message}`, 'error');
                // Store metadata even if download fails
                fileData = Buffer.from(''); 
            }

            // Calculate SHA256
            const sha256Hash = crypto.createHash('sha256').update(fileData).digest('hex');

            // Auto-categorize (simple approach)
            const category = this.guessCategory(file.name, mimeType);

            // Insert into database
            await this.pool.query(
                `INSERT INTO imported_assets 
                 (filename, category, mime_type, file_size, file_data, sha256_hash, 
                  drive_file_id, drive_path, processing_stage, imported_at)
                 VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, NOW())
                 ON CONFLICT (drive_file_id) DO NOTHING`,
                [
                    file.name,
                    category,
                    mimeType,
                    parseInt(file.size) || 0,
                    fileData,
                    sha256Hash,
                    file.id,
                    path + file.name,
                    'completed'
                ]
            );

            this.totalCopied++;
            this.logMessage(`✅ Copied: ${file.name} → ${category}`, 'success');

        } catch (error) {
            this.logMessage(`❌ Error copying ${file.name}: ${error.message}`, 'error');
            this.errors.push({ filename: file.name, error: error.message });
        }
    }

    guessCategory(filename, mimeType) {
        const lower = filename.toLowerCase();
        
        // CRITICAL: ZIP files are loaded with important info - categorize carefully
        if (lower.endsWith('.zip') || lower.endsWith('.rar') || lower.endsWith('.7z') || 
            mimeType === 'application/zip' || mimeType === 'application/x-zip-compressed') {
            
            // Guess category based on ZIP filename
            if (lower.includes('solver') || lower.includes('bitcrack') || lower.includes('kangaroo')) {
                return 'solvers';
            }
            if (lower.includes('puzzle')) {
                return 'puzzles';
            }
            if (lower.includes('tool')) {
                return 'tools';
            }
            if (lower.includes('key') || lower.includes('address')) {
                return 'keys';
            }
            if (lower.includes('wordlist') || lower.includes('bloom')) {
                return 'wordlists';
            }
            // Default for ZIPs - user will sort later
            return 'archives';
        }
        
        // Simple categorization - just guess, user will clean up later
        if (lower.includes('bitcrack') || lower.includes('kangaroo') || lower.includes('keyhunt')) {
            return 'solvers';
        }
        if (lower.includes('puzzle') || lower.includes('challenge')) {
            return 'puzzles';
        }
        if (lower.includes('key') && (lower.endsWith('.txt') || lower.endsWith('.json'))) {
            return 'keys';
        }
        if (lower.includes('address')) {
            return 'addresses';
        }
        if (lower.includes('api') || lower.includes('config')) {
            return 'config';
        }
        if (lower.includes('wordlist') || lower.includes('bloom')) {
            return 'wordlists';
        }
        if (mimeType.startsWith('image/')) {
            return 'screenshots';
        }
        if (lower.endsWith('.exe') || lower.endsWith('.bin') || lower.endsWith('.app')) {
            return 'tools';
        }
        if (lower.endsWith('.txt')) {
            return 'docs';
        }
        if (lower.endsWith('.csv') || lower.endsWith('.db') || lower.endsWith('.sqlite')) {
            return 'databases';
        }
        
        return 'general'; // Everything else - user sorts later
    }

    formatBytes(bytes) {
        if (!bytes || bytes === '0') return '0 B';
        const k = 1024;
        const sizes = ['B', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
    }

    async runFullCopy() {
        try {
            this.logMessage('═══════════════════════════════════════════════════════════');
            this.logMessage('🚀 AUTO-COPY ALL DRIVE FILES - STARTING');
            this.logMessage('   Strategy: Copy EVERYTHING, delete junk later');
            this.logMessage('═══════════════════════════════════════════════════════════');

            const startTime = Date.now();

            // Copy everything from root
            await this.copyEverythingFromDrive();

            const duration = ((Date.now() - startTime) / 1000 / 60).toFixed(2);

            this.logMessage('═══════════════════════════════════════════════════════════');
            this.logMessage('✅ AUTO-COPY COMPLETE!');
            this.logMessage(`   Total files copied: ${this.totalCopied}`);
            this.logMessage(`   Errors: ${this.errors.length}`);
            this.logMessage(`   Duration: ${duration} minutes`);
            this.logMessage('   Now you can delete duplicates/junk manually!');
            this.logMessage('═══════════════════════════════════════════════════════════');

            return {
                success: true,
                totalCopied: this.totalCopied,
                errors: this.errors,
                duration: duration
            };

        } catch (error) {
            this.logMessage(`FATAL ERROR: ${error.message}`, 'error');
            return {
                success: false,
                error: error.message,
                totalCopied: this.totalCopied,
                errors: this.errors
            };
        }
    }

    getStatus() {
        return {
            totalCopied: this.totalCopied,
            errors: this.errors,
            log: this.log.slice(-50)
        };
    }
}

module.exports = AutoCopyAllDriveFiles;
