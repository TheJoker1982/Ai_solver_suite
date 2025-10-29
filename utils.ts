import JSZip from 'jszip';

async function readFileAsText(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = (error) => reject(error);
        reader.readAsText(file);
    });
}

async function readZipFile(file: File): Promise<string> {
    const zip = new JSZip();
    const contents = await zip.loadAsync(file);
    const fileContents: string[] = [];
    const filePromises: Promise<void>[] = [];

    for (const filename of Object.keys(contents.files)) {
        const zipEntry = contents.files[filename];
        if (!zipEntry.dir) {
            const promise = (async () => {
                try {
                    const content = await zipEntry.async('string');
                    fileContents.push(`--- File: ${filename} ---\n\n${content}\n\n`);
                } catch (e) {
                    fileContents.push(`--- File: ${filename} (skipped as non-text) ---\n\n`);
                }
            })();
            filePromises.push(promise);
        }
    }
    await Promise.all(filePromises);
    return fileContents.join('');
}


export async function processFile(file: File): Promise<string> {
    const extension = file.name.split('.').pop()?.toLowerCase();
    
    if (extension === 'zip') {
        return readZipFile(file);
    } 
    
    // Check for common text-based mime types and extensions
    if (file.type.startsWith('text/') || ['json', 'csv', 'html'].includes(extension || '') || file.type === 'application/json') {
        return readFileAsText(file);
    }
    
    throw new Error(`Unsupported file type: .${extension}. Please upload a zip, json, csv, html, or other text-based file.`);
}
