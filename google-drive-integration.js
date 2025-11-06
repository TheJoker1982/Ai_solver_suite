import { google } from 'googleapis';

let connectionSettings;

async function getAccessToken() {
  if (connectionSettings && connectionSettings.settings.expires_at && new Date(connectionSettings.settings.expires_at).getTime() > Date.now()) {
    return connectionSettings.settings.access_token;
  }
  
  const hostname = process.env.REPLIT_CONNECTORS_HOSTNAME;
  const xReplitToken = process.env.REPL_IDENTITY 
    ? 'repl ' + process.env.REPL_IDENTITY 
    : process.env.WEB_REPL_RENEWAL 
    ? 'depl ' + process.env.WEB_REPL_RENEWAL 
    : null;

  if (!xReplitToken) {
    throw new Error('X_REPLIT_TOKEN not found for repl/depl');
  }

  connectionSettings = await fetch(
    'https://' + hostname + '/api/v2/connection?include_secrets=true&connector_names=google-drive',
    {
      headers: {
        'Accept': 'application/json',
        'X_REPLIT_TOKEN': xReplitToken
      }
    }
  ).then(res => res.json()).then(data => data.items?.[0]);

  const accessToken = connectionSettings?.settings?.access_token || connectionSettings.settings?.oauth?.credentials?.access_token;

  if (!connectionSettings || !accessToken) {
    throw new Error('Google Drive not connected');
  }
  return accessToken;
}

// WARNING: Never cache this client.
// Access tokens expire, so a new client must be created each time.
export async function getUncachableGoogleDriveClient() {
  const accessToken = await getAccessToken();

  const oauth2Client = new google.auth.OAuth2();
  oauth2Client.setCredentials({
    access_token: accessToken
  });

  return google.drive({ version: 'v3', auth: oauth2Client });
}

// Utility functions for common Google Drive operations

export async function listFiles(folderId = 'root', pageSize = 100) {
  const drive = await getUncachableGoogleDriveClient();
  
  const response = await drive.files.list({
    q: `'${folderId}' in parents and trashed = false`,
    pageSize: pageSize,
    fields: 'nextPageToken, files(id, name, mimeType, size, modifiedTime, createdTime, webViewLink, thumbnailLink)',
    orderBy: 'name'
  });

  return response.data.files;
}

export async function listFolders(parentId = 'root') {
  const drive = await getUncachableGoogleDriveClient();
  
  const response = await drive.files.list({
    q: `'${parentId}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false`,
    fields: 'files(id, name, mimeType, modifiedTime)',
    orderBy: 'name'
  });

  return response.data.files;
}

export async function downloadFile(fileId) {
  const drive = await getUncachableGoogleDriveClient();
  
  const response = await drive.files.get({
    fileId: fileId,
    alt: 'media'
  }, { responseType: 'stream' });

  return response.data;
}

export async function getFileMetadata(fileId) {
  const drive = await getUncachableGoogleDriveClient();
  
  const response = await drive.files.get({
    fileId: fileId,
    fields: 'id, name, mimeType, size, modifiedTime, createdTime, webViewLink, thumbnailLink, description'
  });

  return response.data;
}

export async function searchFiles(query) {
  const drive = await getUncachableGoogleDriveClient();
  
  const response = await drive.files.list({
    q: `name contains '${query}' and trashed = false`,
    pageSize: 50,
    fields: 'files(id, name, mimeType, size, modifiedTime, webViewLink)',
    orderBy: 'modifiedTime desc'
  });

  return response.data.files;
}

export async function uploadFile(fileName, fileContent, mimeType, folderId = 'root') {
  const drive = await getUncachableGoogleDriveClient();
  
  const fileMetadata = {
    name: fileName,
    parents: [folderId]
  };

  const media = {
    mimeType: mimeType,
    body: fileContent
  };

  const response = await drive.files.create({
    requestBody: fileMetadata,
    media: media,
    fields: 'id, name, webViewLink'
  });

  return response.data;
}

export async function getDriveInfo() {
  const drive = await getUncachableGoogleDriveClient();
  
  const response = await drive.about.get({
    fields: 'user, storageQuota'
  });

  return response.data;
}

export async function listAllFilesRecursive(folderId = 'root', depth = 0, maxDepth = 5) {
  if (depth > maxDepth) return [];
  
  const files = await listFiles(folderId);
  const folders = files.filter(f => f.mimeType === 'application/vnd.google-apps.folder');
  const nonFolders = files.filter(f => f.mimeType !== 'application/vnd.google-apps.folder');
  
  let allFiles = [...nonFolders];
  
  for (const folder of folders) {
    const subFiles = await listAllFilesRecursive(folder.id, depth + 1, maxDepth);
    allFiles = [...allFiles, ...subFiles];
  }
  
  return allFiles;
}
