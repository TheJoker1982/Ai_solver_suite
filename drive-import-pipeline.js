const crypto = require('crypto');
const { google } = require('googleapis');

class DriveImportPipeline {
    constructor(pool) {
        this.pool = pool;
        this.cryptoKeywords = [
            'bitcoin', 'btc', 'ethereum', 'eth', 'crypto', 'wallet', 'key', 'private',
            'public', 'address', 'puzzle', 'hash', 'blockchain', 'satoshi', 'seed',
            'mnemonic', 'wif', 'hex', 'base58', 'bip32', 'bip39', 'hdwallet', 'ecdsa',
            'secp256k1', 'ripemd', 'sha256', 'transaction', 'utxo', 'mining', 'block',
            'coinbase', 'litecoin', 'dogecoin', 'monero', 'zcash', 'dash', 'ripple',
            'stellar', 'cardano', 'polkadot', 'solana', 'defi', 'nft', 'token', 'erc20',
            'smart contract', 'web3', 'metamask', 'ledger', 'trezor', 'cold storage',
            'paper wallet', 'brain wallet', 'vanity address', 'multisig', 'signing',
            'verify', 'decrypt', 'encrypt', 'cipher', 'brute', 'crack', 'scan'
        ];
        
        this.categoryPatterns = {
            'puzzles': ['puzzle', 'challenge', 'unsolved', 'btc puzzle', 'privatekeys.pw'],
            'wallets': ['wallet', 'electrum', 'core', 'armory', 'exodus', 'trust wallet'],
            'keys': ['private key', 'public key', 'wif', 'seed', 'mnemonic', 'recovery'],
            'tools': ['tool', 'script', 'program', 'software', 'scanner', 'generator'],
            'documentation': ['guide', 'tutorial', 'manual', 'readme', 'doc', 'pdf', 'whitepaper'],
            'data': ['database', 'list', 'addresses', 'hashes', 'bloom', 'dataset'],
            'code': ['.py', '.js', '.go', '.rs', '.c', '.cpp', '.java', 'source', 'repo'],
            'research': ['research', 'paper', 'analysis', 'study', 'report', 'findings']
        };
    }

    async getGoogleDriveClient() {
        const hostname = process.env.REPLIT_CONNECTORS_HOSTNAME;
        const xReplitToken = process.env.REPL_IDENTITY 
            ? 'repl ' + process.env.REPL_IDENTITY 
            : process.env.WEB_REPL_RENEWAL 
            ? 'depl ' + process.env.WEB_REPL_RENEWAL 
            : null;

        if (!xReplitToken) {
            throw new Error('Authentication token not found');
        }

        const connectionSettings = await fetch(
            'https://' + hostname + '/api/v2/connection?include_secrets=true&connector_names=google-drive',
            {
                headers: {
                    'Accept': 'application/json',
                    'X_REPLIT_TOKEN': xReplitToken
                }
            }
        ).then(res => res.json()).then(data => data.items?.[0]);

        const accessToken = connectionSettings?.settings?.access_token || 
                           connectionSettings?.settings?.oauth?.credentials?.access_token;

        if (!connectionSettings || !accessToken) {
            throw new Error('Google Drive not connected');
        }

        const oauth2Client = new google.auth.OAuth2();
        oauth2Client.setCredentials({ access_token: accessToken });

        return google.drive({ version: 'v3', auth: oauth2Client });
    }

    isCryptoRelated(filename, mimeType) {
        const lowerName = filename.toLowerCase();
        return this.cryptoKeywords.some(keyword => lowerName.includes(keyword));
    }

    determineCategory(filename, folderPath = '') {
        const lowerName = filename.toLowerCase();
        const lowerPath = folderPath.toLowerCase();
        const combined = lowerName + ' ' + lowerPath;

        let bestCategory = 'general';
        let highestConfidence = 0;

        for (const [category, patterns] of Object.entries(this.categoryPatterns)) {
            let matches = 0;
            for (const pattern of patterns) {
                if (combined.includes(pattern)) {
                    matches++;
                }
            }
            const confidence = matches / patterns.length;
            if (confidence > highestConfidence) {
                highestConfidence = confidence;
                bestCategory = category;
            }
        }

        return { category: bestCategory, confidence: highestConfidence };
    }

    calculateSHA256(buffer) {
        return crypto.createHash('sha256').update(buffer).digest('hex');
    }

    normalizeFilename(filename) {
        return filename
            .toLowerCase()
            .replace(/\s+/g, '_')
            .replace(/[^a-z0-9._-]/g, '')
            .replace(/_+/g, '_');
    }

    async createImportRun(runName, config = {}) {
        const result = await this.pool.query(
            `INSERT INTO import_runs (run_name, config, created_by, status)
             VALUES ($1, $2, $3, 'running')
             RETURNING id`,
            [runName, JSON.stringify(config), 'admin']
        );
        return result.rows[0].id;
    }

    async updateImportRunProgress(runId, updates) {
        const setClause = Object.keys(updates)
            .map((key, idx) => `${key} = $${idx + 2}`)
            .join(', ');
        
        const values = [runId, ...Object.values(updates)];
        
        await this.pool.query(
            `UPDATE import_runs SET ${setClause} WHERE id = $1`,
            values
        );
    }

    async discoverFiles(runId, folderId = 'root', parentPath = '', drive = null) {
        if (!drive) {
            drive = await this.getGoogleDriveClient();
        }

        let discoveredFiles = [];
        let pageToken = null;
        let totalFound = 0;

        do {
            try {
                const response = await drive.files.list({
                    q: `'${folderId}' in parents and trashed = false`,
                    pageSize: 250,
                    fields: 'nextPageToken, files(id, name, mimeType, size, modifiedTime, parents)',
                    orderBy: 'name',
                    pageToken: pageToken
                });

                const files = response.data.files || [];
                totalFound += files.length;

                for (const file of files) {
                    const filePath = parentPath ? `${parentPath}/${file.name}` : file.name;

                    if (file.mimeType === 'application/vnd.google-apps.folder') {
                        await this.pool.query(
                            `INSERT INTO drive_discovery_jobs 
                             (import_run_id, folder_id, folder_name, parent_path, status)
                             VALUES ($1, $2, $3, $4, 'pending')`,
                            [runId, file.id, file.name, parentPath]
                        );
                    } else if (this.isCryptoRelated(file.name, file.mimeType)) {
                        const { category, confidence } = this.determineCategory(file.name, parentPath);
                        
                        discoveredFiles.push({
                            driveFileId: file.id,
                            filename: file.name,
                            mimeType: file.mimeType,
                            fileSize: parseInt(file.size) || 0,
                            category: category,
                            confidence: confidence,
                            drivePath: filePath,
                            modifiedTime: file.modifiedTime
                        });
                    }
                }

                pageToken = response.data.nextPageToken;

                await this.updateImportRunProgress(runId, {
                    total_files_discovered: totalFound,
                    current_folder: parentPath || 'root'
                });

                if (files.length > 0) {
                    await new Promise(resolve => setTimeout(resolve, 350));
                }

            } catch (error) {
                console.error(`Error discovering files in ${parentPath}:`, error.message);
                break;
            }
        } while (pageToken);

        return discoveredFiles;
    }

    async processDiscoveredFile(file, runId, drive = null) {
        if (!drive) {
            drive = await this.getGoogleDriveClient();
        }

        try {
            const existingByHash = await this.pool.query(
                'SELECT id FROM imported_assets WHERE drive_file_id = $1',
                [file.driveFileId]
            );

            if (existingByHash.rows.length > 0) {
                await this.pool.query(
                    `UPDATE imported_assets 
                     SET source_drive_paths = source_drive_paths || $1::jsonb
                     WHERE id = $2`,
                    [JSON.stringify([file.drivePath]), existingByHash.rows[0].id]
                );
                
                await this.updateImportRunProgress(runId, {
                    total_duplicates_skipped: 1
                });
                
                return { skipped: true, reason: 'duplicate_drive_id' };
            }

            const fileData = await drive.files.get({
                fileId: file.driveFileId,
                alt: 'media'
            }, { responseType: 'arraybuffer' });

            const buffer = Buffer.from(fileData.data);
            const sha256 = this.calculateSHA256(buffer);

            const existingHash = await this.pool.query(
                'SELECT id FROM imported_assets WHERE sha256_hash = $1',
                [sha256]
            );

            if (existingHash.rows.length > 0) {
                await this.pool.query(
                    `INSERT INTO asset_duplicates 
                     (canonical_asset_id, duplicate_drive_id, duplicate_path, similarity_score)
                     VALUES ($1, $2, $3, 1.0)`,
                    [existingHash.rows[0].id, file.driveFileId, file.drivePath]
                );

                await this.updateImportRunProgress(runId, {
                    total_duplicates_skipped: 1
                });

                return { skipped: true, reason: 'duplicate_content', canonicalId: existingHash.rows[0].id };
            }

            const normalizedName = this.normalizeFilename(file.filename);
            const keywords = this.cryptoKeywords.filter(kw => 
                file.filename.toLowerCase().includes(kw) || 
                file.drivePath.toLowerCase().includes(kw)
            );

            const result = await this.pool.query(
                `INSERT INTO imported_assets 
                 (drive_file_id, filename, normalized_filename, mime_type, file_size, 
                  category, file_data, sha256_hash, source_drive_paths, 
                  auto_category_confidence, keywords, processing_stage, imported_by, imported_at)
                 VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, 'completed', 'pipeline', NOW())
                 RETURNING id, filename, category`,
                [
                    file.driveFileId,
                    file.filename,
                    normalizedName,
                    file.mimeType,
                    file.fileSize,
                    file.category,
                    buffer,
                    sha256,
                    JSON.stringify([file.drivePath]),
                    file.confidence,
                    keywords
                ]
            );

            await this.updateImportRunProgress(runId, {
                total_files_downloaded: 1,
                total_bytes_processed: file.fileSize
            });

            return { 
                success: true, 
                assetId: result.rows[0].id,
                filename: result.rows[0].filename,
                category: result.rows[0].category
            };

        } catch (error) {
            console.error(`Error processing ${file.filename}:`, error.message);
            return { error: error.message };
        }
    }

    async runFullImport(runName = 'Crypto Files Import') {
        console.log('🚀 Starting comprehensive crypto file import...');
        
        const runId = await this.createImportRun(runName, {
            keywords: this.cryptoKeywords,
            categories: Object.keys(this.categoryPatterns)
        });

        console.log(`📋 Import Run ID: ${runId}`);

        const drive = await this.getGoogleDriveClient();

        console.log('🔍 Stage 1: Discovering files in root folder...');
        const rootFiles = await this.discoverFiles(runId, 'root', '', drive);
        console.log(`   Found ${rootFiles.length} crypto-related files in root`);

        console.log('🔍 Stage 2: Processing subfolders...');
        const pendingFolders = await this.pool.query(
            'SELECT * FROM drive_discovery_jobs WHERE import_run_id = $1 AND status = $2 ORDER BY id',
            [runId, 'pending']
        );

        let allDiscoveredFiles = [...rootFiles];

        for (const folder of pendingFolders.rows) {
            console.log(`   📁 Scanning: ${folder.parent_path}/${folder.folder_name}`);
            
            const folderFiles = await this.discoverFiles(
                runId, 
                folder.folder_id, 
                `${folder.parent_path}/${folder.folder_name}`,
                drive
            );
            
            allDiscoveredFiles = allDiscoveredFiles.concat(folderFiles);
            
            await this.pool.query(
                'UPDATE drive_discovery_jobs SET status = $1, files_found = $2, processed_at = NOW() WHERE id = $3',
                ['completed', folderFiles.length, folder.id]
            );
            
            console.log(`      Found ${folderFiles.length} crypto files`);
        }

        console.log(`\n📊 Discovery Complete: ${allDiscoveredFiles.length} crypto-related files found`);
        console.log('💾 Stage 3: Downloading and deduplicating files...\n');

        let imported = 0;
        let skipped = 0;
        let errors = 0;

        for (let i = 0; i < allDiscoveredFiles.length; i++) {
            const file = allDiscoveredFiles[i];
            console.log(`   [${i + 1}/${allDiscoveredFiles.length}] Processing: ${file.filename}`);
            
            const result = await this.processDiscoveredFile(file, runId, drive);
            
            if (result.success) {
                imported++;
                console.log(`      ✅ Imported as ${result.category} (ID: ${result.assetId})`);
            } else if (result.skipped) {
                skipped++;
                console.log(`      ⏭️  Skipped: ${result.reason}`);
            } else if (result.error) {
                errors++;
                console.log(`      ❌ Error: ${result.error}`);
            }

            if ((i + 1) % 10 === 0) {
                await new Promise(resolve => setTimeout(resolve, 500));
            }
        }

        await this.pool.query(
            `UPDATE import_runs 
             SET status = 'completed', completed_at = NOW()
             WHERE id = $1`,
            [runId]
        );

        console.log('\n✅ Import Complete!');
        console.log(`   📥 Imported: ${imported} files`);
        console.log(`   ⏭️  Skipped (duplicates): ${skipped} files`);
        console.log(`   ❌ Errors: ${errors} files`);
        
        return {
            runId,
            imported,
            skipped,
            errors,
            total: allDiscoveredFiles.length
        };
    }
}

module.exports = DriveImportPipeline;
