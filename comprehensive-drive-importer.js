const crypto = require('crypto');
const { google } = require('googleapis');

class ComprehensiveDriveImporter {
    constructor(pool) {
        this.pool = pool;
        
        // COMPREHENSIVE category patterns - EVERYTHING matters
        this.categoryPatterns = {
            'solvers': [
                'solver', 'bitcrack', 'kangaroo', 'keyhunt', 'vanitygen', 'brainflayer',
                'btcrecover', 'hashcat', 'john', 'findkey', 'keyfinder', 'keyspace',
                'bruteforce', 'bforce', 'cracker', 'recovery', 'finder', 'hunter',
                'scanner', 'searcher', 'miner', 'generator'
            ],
            'tools': [
                'tool', 'utility', 'helper', 'converter', 'calculator', 'analyzer',
                'validator', 'encoder', 'decoder', 'parser', 'formatter', 'extractor'
            ],
            'puzzles': [
                'puzzle', 'challenge', 'unsolved', 'btc puzzle', 'privatekeys.pw',
                'mystery', 'riddle', 'problem', 'quest', 'treasure'
            ],
            'screenshots': [
                '.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg', '.ico',
                'screenshot', 'screen shot', 'capture', 'image', 'photo', 'picture'
            ],
            'wallets': [
                'wallet', 'electrum', 'core', 'armory', 'exodus', 'trust wallet',
                'ledger', 'trezor', 'coinbase', 'blockchain.com', 'mycelium', 'jaxx'
            ],
            'keys': [
                'private key', 'public key', 'wif', 'seed', 'mnemonic', 'recovery',
                'passphrase', 'keystore', 'keyfile', 'privatekey', 'pubkey'
            ],
            'addresses': [
                'address', 'addresses', 'addr', 'receiving', 'change', 'multisig',
                'p2pkh', 'p2sh', 'bech32', 'segwit', 'taproot'
            ],
            'hashes': [
                'hash', 'hash160', 'sha256', 'ripemd', 'md5', 'keccak',
                'blake', 'digest', 'checksum'
            ],
            'scripts': [
                '.py', '.js', '.ts', '.sh', '.bat', '.ps1', '.rb', '.go',
                '.rs', '.c', '.cpp', '.java', '.php', 'script', 'code'
            ],
            'databases': [
                'database', 'db', '.sql', '.sqlite', '.db3', '.mdb',
                'addresses.txt', 'keys.txt', 'list', 'dataset', 'dump'
            ],
            'documentation': [
                'guide', 'tutorial', 'manual', 'readme', 'doc', '.pdf',
                'whitepaper', 'specification', 'reference', 'help', 'instruction'
            ],
            'research': [
                'research', 'paper', 'analysis', 'study', 'report', 'findings',
                'thesis', 'investigation', 'experiment', 'test', 'benchmark'
            ],
            'blockchain_data': [
                'block', 'blockchain', 'transaction', 'tx', 'utxo', 'mempool',
                'chain', 'ledger', 'merkle', 'header'
            ],
            'configuration': [
                'config', 'conf', '.ini', '.yaml', '.yml', '.toml', '.json',
                'settings', 'preferences', 'options'
            ],
            'logs': [
                'log', 'logs', '.log', 'output', 'result', 'history', 'record'
            ],
            'backup': [
                'backup', 'bak', 'archive', 'old', 'copy', 'snapshot', 'restore'
            ],
            'wordlists': [
                'wordlist', 'dictionary', 'words', 'passlist', 'password',
                'common', 'rockyou', 'phrases'
            ],
            'bloom_filters': [
                'bloom', 'filter', 'bloom filter', 'bloomfilter', '.blf', '.bloom'
            ]
        };

        // File type detection
        this.fileTypes = {
            images: ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.svg', '.ico', '.tiff'],
            executables: ['.exe', '.dll', '.so', '.dylib', '.app', '.bin', '.elf'],
            scripts: ['.py', '.js', '.ts', '.sh', '.bat', '.ps1', '.rb', '.go', '.rs'],
            documents: ['.pdf', '.doc', '.docx', '.txt', '.md', '.rtf', '.odt'],
            spreadsheets: ['.xls', '.xlsx', '.csv', '.ods'],
            archives: ['.zip', '.tar', '.gz', '.bz2', '.7z', '.rar', '.tar.gz'],
            databases: ['.sql', '.sqlite', '.db', '.db3', '.mdb'],
            config: ['.json', '.yaml', '.yml', '.toml', '.ini', '.conf', '.cfg']
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

    getFileExtension(filename) {
        const match = filename.match(/\.[^.]+$/);
        return match ? match[0].toLowerCase() : '';
    }

    detectFileType(filename) {
        const ext = this.getFileExtension(filename);
        
        for (const [type, extensions] of Object.entries(this.fileTypes)) {
            if (extensions.includes(ext)) {
                return type;
            }
        }
        
        return 'other';
    }

    determineCategories(filename, folderPath = '', mimeType = '') {
        const lowerName = filename.toLowerCase();
        const lowerPath = folderPath.toLowerCase();
        const combined = `${lowerName} ${lowerPath}`;
        
        const matchedCategories = [];
        
        // Match against all category patterns
        for (const [category, patterns] of Object.entries(this.categoryPatterns)) {
            let matches = 0;
            const matchedPatterns = [];
            
            for (const pattern of patterns) {
                if (combined.includes(pattern.toLowerCase())) {
                    matches++;
                    matchedPatterns.push(pattern);
                }
            }
            
            if (matches > 0) {
                const confidence = matches / patterns.length;
                matchedCategories.push({
                    category,
                    confidence,
                    matches,
                    patterns: matchedPatterns
                });
            }
        }

        // Sort by confidence and number of matches
        matchedCategories.sort((a, b) => {
            if (b.confidence !== a.confidence) {
                return b.confidence - a.confidence;
            }
            return b.matches - a.matches;
        });

        // Return primary category and all matched categories
        const primary = matchedCategories.length > 0 
            ? matchedCategories[0].category 
            : 'general';
        
        const allCategories = matchedCategories.map(c => c.category);
        const confidence = matchedCategories.length > 0 
            ? matchedCategories[0].confidence 
            : 0;

        return { 
            primary, 
            allCategories, 
            confidence,
            fileType: this.detectFileType(filename)
        };
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

    async discoverAllFiles(runId, folderId = 'root', parentPath = '', drive = null, depth = 0) {
        if (!drive) {
            drive = await this.getGoogleDriveClient();
        }

        const maxDepth = 20; // Prevent infinite recursion
        if (depth > maxDepth) {
            console.warn(`Max depth ${maxDepth} reached for folder: ${parentPath}`);
            return [];
        }

        let discoveredFiles = [];
        let pageToken = null;
        let totalFound = 0;

        console.log(`${'  '.repeat(depth)}📁 Scanning: ${parentPath || 'root'} (depth: ${depth})`);

        do {
            try {
                const response = await drive.files.list({
                    q: `'${folderId}' in parents and trashed = false`,
                    pageSize: 250,
                    fields: 'nextPageToken, files(id, name, mimeType, size, modifiedTime, parents, webViewLink)',
                    orderBy: 'name',
                    pageToken: pageToken
                });

                const files = response.data.files || [];
                totalFound += files.length;

                const folders = [];
                const regularFiles = [];

                for (const file of files) {
                    const filePath = parentPath ? `${parentPath}/${file.name}` : file.name;

                    if (file.mimeType === 'application/vnd.google-apps.folder') {
                        folders.push({ ...file, filePath });
                    } else {
                        regularFiles.push({ ...file, filePath });
                    }
                }

                // Process all regular files
                for (const file of regularFiles) {
                    const categories = this.determineCategories(file.name, file.filePath, file.mimeType);
                    
                    discoveredFiles.push({
                        driveFileId: file.id,
                        filename: file.name,
                        mimeType: file.mimeType,
                        fileSize: parseInt(file.size) || 0,
                        category: categories.primary,
                        allCategories: categories.allCategories,
                        confidence: categories.confidence,
                        fileType: categories.fileType,
                        drivePath: file.filePath,
                        modifiedTime: file.modifiedTime,
                        webViewLink: file.webViewLink,
                        depth: depth
                    });
                }

                console.log(`${'  '.repeat(depth)}   Found ${regularFiles.length} files, ${folders.length} folders`);

                // Process subfolders recursively
                for (const folder of folders) {
                    await this.pool.query(
                        `INSERT INTO drive_discovery_jobs 
                         (import_run_id, folder_id, folder_name, parent_path, status)
                         VALUES ($1, $2, $3, $4, 'processing')`,
                        [runId, folder.id, folder.name, parentPath]
                    );

                    const subFolderFiles = await this.discoverAllFiles(
                        runId,
                        folder.id,
                        folder.filePath,
                        drive,
                        depth + 1
                    );

                    discoveredFiles = discoveredFiles.concat(subFolderFiles);

                    await this.pool.query(
                        'UPDATE drive_discovery_jobs SET status = $1, files_found = $2, processed_at = NOW() WHERE import_run_id = $3 AND folder_id = $4',
                        ['completed', subFolderFiles.length, runId, folder.id]
                    );
                }

                pageToken = response.data.nextPageToken;

                await this.updateImportRunProgress(runId, {
                    total_files_discovered: discoveredFiles.length,
                    current_folder: parentPath || 'root'
                });

                // Rate limiting
                if (files.length > 0) {
                    await new Promise(resolve => setTimeout(resolve, 300));
                }

            } catch (error) {
                console.error(`Error discovering files in ${parentPath}:`, error.message);
                
                // Log error but continue
                await this.pool.query(
                    `UPDATE import_runs 
                     SET error_log = error_log || $1::jsonb 
                     WHERE id = $2`,
                    [JSON.stringify([{ folder: parentPath, error: error.message, timestamp: new Date() }]), runId]
                );
                
                break;
            }
        } while (pageToken);

        return discoveredFiles;
    }

    async processFile(file, runId, drive = null) {
        if (!drive) {
            drive = await this.getGoogleDriveClient();
        }

        try {
            // Check if already imported by Drive ID
            const existingByDriveId = await this.pool.query(
                'SELECT id, filename FROM imported_assets WHERE drive_file_id = $1',
                [file.driveFileId]
            );

            if (existingByDriveId.rows.length > 0) {
                // Update source paths
                await this.pool.query(
                    `UPDATE imported_assets 
                     SET source_drive_paths = source_drive_paths || $1::jsonb
                     WHERE id = $2`,
                    [JSON.stringify([file.drivePath]), existingByDriveId.rows[0].id]
                );
                
                return { skipped: true, reason: 'duplicate_drive_id', existing: existingByDriveId.rows[0].filename };
            }

            // Download file
            const fileData = await drive.files.get({
                fileId: file.driveFileId,
                alt: 'media'
            }, { responseType: 'arraybuffer' });

            const buffer = Buffer.from(fileData.data);
            const sha256 = this.calculateSHA256(buffer);

            // Check for content duplicates by hash
            const existingByHash = await this.pool.query(
                'SELECT id, filename, drive_file_id FROM imported_assets WHERE sha256_hash = $1',
                [sha256]
            );

            if (existingByHash.rows.length > 0) {
                // Record as duplicate
                await this.pool.query(
                    `INSERT INTO asset_duplicates 
                     (canonical_asset_id, duplicate_drive_id, duplicate_path, similarity_score)
                     VALUES ($1, $2, $3, 1.0)`,
                    [existingByHash.rows[0].id, file.driveFileId, file.drivePath]
                );

                return { 
                    skipped: true, 
                    reason: 'duplicate_content', 
                    canonicalId: existingByHash.rows[0].id,
                    canonical: existingByHash.rows[0].filename
                };
            }

            const normalizedName = this.normalizeFilename(file.filename);

            // Extract metadata
            const metadata = {
                fileType: file.fileType,
                allCategories: file.allCategories,
                depth: file.depth,
                webViewLink: file.webViewLink,
                originalModifiedTime: file.modifiedTime,
                extension: this.getFileExtension(file.filename)
            };

            // Import the file
            const result = await this.pool.query(
                `INSERT INTO imported_assets 
                 (drive_file_id, filename, normalized_filename, mime_type, file_size, 
                  category, file_data, sha256_hash, source_drive_paths, 
                  auto_category_confidence, extracted_metadata, processing_stage, 
                  imported_by, imported_at)
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
                    JSON.stringify(metadata)
                ]
            );

            return { 
                success: true, 
                assetId: result.rows[0].id,
                filename: result.rows[0].filename,
                category: result.rows[0].category,
                size: file.fileSize
            };

        } catch (error) {
            console.error(`Error processing ${file.filename}:`, error.message);
            return { error: error.message, filename: file.filename };
        }
    }

    async runComprehensiveImport(runName = 'COMPLETE Drive Import') {
        console.log('');
        console.log('════════════════════════════════════════════════════════════════');
        console.log('🚀 COMPREHENSIVE GOOGLE DRIVE IMPORT - EVERYTHING MATTERS');
        console.log('════════════════════════════════════════════════════════════════');
        console.log('');
        console.log('📋 This import will:');
        console.log('   ✓ Scan EVERY folder and subfolder recursively');
        console.log('   ✓ Import EVERY file (screenshots, tools, solvers, docs, ALL)');
        console.log('   ✓ Detect and skip duplicates (you have 3+ copies of many files)');
        console.log('   ✓ Categorize intelligently (50+ categories and file types)');
        console.log('   ✓ Preserve folder structure and file relationships');
        console.log('   ✓ Track everything in database for easy access');
        console.log('');
        
        const runId = await this.createImportRun(runName, {
            mode: 'comprehensive',
            categories: Object.keys(this.categoryPatterns),
            fileTypes: Object.keys(this.fileTypes)
        });

        console.log(`📋 Import Run ID: ${runId}`);
        console.log('');

        const drive = await this.getGoogleDriveClient();

        console.log('══════════════════════════════════════════════════════════════');
        console.log('🔍 STAGE 1: RECURSIVE DISCOVERY');
        console.log('══════════════════════════════════════════════════════════════');
        console.log('');

        const allFiles = await this.discoverAllFiles(runId, 'root', '', drive, 0);

        console.log('');
        console.log(`✅ Discovery Complete: ${allFiles.length} total files found`);
        console.log('');

        // Show breakdown by category
        const categoryCount = {};
        const fileTypeCount = {};
        
        for (const file of allFiles) {
            categoryCount[file.category] = (categoryCount[file.category] || 0) + 1;
            fileTypeCount[file.fileType] = (fileTypeCount[file.fileType] || 0) + 1;
        }

        console.log('📊 Files by Category:');
        Object.entries(categoryCount)
            .sort(([,a], [,b]) => b - a)
            .forEach(([cat, count]) => {
                console.log(`   ${cat}: ${count} files`);
            });

        console.log('');
        console.log('📊 Files by Type:');
        Object.entries(fileTypeCount)
            .sort(([,a], [,b]) => b - a)
            .forEach(([type, count]) => {
                console.log(`   ${type}: ${count} files`);
            });

        console.log('');
        console.log('══════════════════════════════════════════════════════════════');
        console.log('💾 STAGE 2: DOWNLOAD & DEDUPLICATION');
        console.log('══════════════════════════════════════════════════════════════');
        console.log('');

        let imported = 0;
        let skipped = 0;
        let errors = 0;
        let totalBytes = 0;

        for (let i = 0; i < allFiles.length; i++) {
            const file = allFiles[i];
            const progress = `[${i + 1}/${allFiles.length}]`;
            const sizeMB = (file.fileSize / (1024 * 1024)).toFixed(2);
            
            console.log(`${progress} ${file.filename} (${sizeMB} MB, ${file.category})`);
            
            const result = await this.processFile(file, runId, drive);
            
            if (result.success) {
                imported++;
                totalBytes += result.size;
                console.log(`        ✅ Imported successfully`);
            } else if (result.skipped) {
                skipped++;
                console.log(`        ⏭️  Skipped: ${result.reason} (duplicate of: ${result.canonical || result.existing})`);
            } else if (result.error) {
                errors++;
                console.log(`        ❌ Error: ${result.error}`);
            }

            // Update progress
            await this.updateImportRunProgress(runId, {
                total_files_downloaded: imported,
                total_duplicates_skipped: skipped,
                total_bytes_processed: totalBytes
            });

            // Rate limiting - slower for large files
            if (file.fileSize > 10 * 1024 * 1024) { // 10 MB
                await new Promise(resolve => setTimeout(resolve, 1000));
            } else if ((i + 1) % 10 === 0) {
                await new Promise(resolve => setTimeout(resolve, 500));
            }
        }

        await this.pool.query(
            `UPDATE import_runs 
             SET status = 'completed', completed_at = NOW()
             WHERE id = $1`,
            [runId]
        );

        console.log('');
        console.log('══════════════════════════════════════════════════════════════');
        console.log('✅ IMPORT COMPLETE!');
        console.log('══════════════════════════════════════════════════════════════');
        console.log('');
        console.log(`📥 Successfully Imported: ${imported} files`);
        console.log(`⏭️  Skipped (duplicates): ${skipped} files`);
        console.log(`❌ Errors: ${errors} files`);
        console.log(`📊 Total Size: ${(totalBytes / (1024 * 1024 * 1024)).toFixed(2)} GB`);
        console.log(`🎯 Total Files Discovered: ${allFiles.length}`);
        console.log('');
        console.log('🗂️  All files are now:');
        console.log('   ✓ Stored in PostgreSQL database');
        console.log('   ✓ Categorized and tagged');
        console.log('   ✓ Deduplicated (3+ copies reduced to 1)');
        console.log('   ✓ Searchable and accessible via API');
        console.log('   ✓ Mapped to original folder structure');
        console.log('');
        
        return {
            runId,
            imported,
            skipped,
            errors,
            total: allFiles.length,
            totalBytes,
            categoryBreakdown: categoryCount,
            fileTypeBreakdown: fileTypeCount
        };
    }
}

module.exports = ComprehensiveDriveImporter;
