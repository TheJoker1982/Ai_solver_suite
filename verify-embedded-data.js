const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const dataFiles = [
  'app-data/puzzles-database.json',
  'app-data/tools-database.json',
  'app-data/character-sets-database.json',
  'app-data/game-content.json',
  'app-data/app-config.json',
  'knowledge-bank.json'
];

console.log('🔍 Verifying embedded data files for app store build...\n');

let totalSize = 0;
let allValid = true;
const checksums = {};

dataFiles.forEach(file => {
  try {
    const content = fs.readFileSync(file, 'utf8');
    const data = JSON.parse(content);
    const stats = fs.statSync(file);
    const sizeKB = (stats.size / 1024).toFixed(2);
    totalSize += stats.size;
    
    const checksum = crypto.createHash('sha256').update(content).digest('hex').substring(0, 16);
    checksums[file] = checksum;
    
    console.log(`✅ ${file}`);
    console.log(`   Size: ${sizeKB} KB`);
    console.log(`   Version: ${data.version || 'N/A'}`);
    console.log(`   Checksum: ${checksum}\n`);
  } catch (error) {
    console.log(`❌ ${file}: ${error.message}\n`);
    allValid = false;
  }
});

console.log(`📊 Total embedded data size: ${(totalSize / 1024).toFixed(2)} KB`);
console.log(`📱 App overhead: ~${(totalSize / 1024).toFixed(0)} KB added to app bundle\n`);

if (allValid) {
  console.log('✅ All data files valid and ready for app store distribution!\n');
  
  console.log('📋 Build Checklist:');
  console.log('   [ ] Data files verified (DONE)');
  console.log('   [ ] Backend API configured');
  console.log('   [ ] Payment integration tested');
  console.log('   [ ] Privacy policy URL added');
  console.log('   [ ] Terms of service URL added');
  console.log('   [ ] Screenshots prepared');
  console.log('   [ ] App icon created (1024x1024)');
  console.log('   [ ] Code obfuscation enabled');
  console.log('   [ ] Analytics configured\n');
  
  fs.writeFileSync('.data-checksums.json', JSON.stringify(checksums, null, 2));
  console.log('💾 Checksums saved to .data-checksums.json\n');
} else {
  console.log('❌ Some files have errors - fix before building\n');
}

process.exit(allValid ? 0 : 1);
