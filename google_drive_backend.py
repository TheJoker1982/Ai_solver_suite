
#!/usr/bin/env python3
"""
Google Drive Backend Integration
Provides access to Google Drive files as backend storage
"""

import os
import io
import json
import logging
from pathlib import Path
from typing import List, Dict, Optional, BinaryIO
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class GoogleDriveBackend:
    """Google Drive backend for file storage and access"""
    
    def __init__(self, credentials_path: str = 'credentials.json', token_path: str = 'token.json'):
        """
        Initialize Google Drive backend
        Args:
            credentials_path: Path to OAuth credentials file
            token_path: Path to store access token
        """
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Google Drive API"""
        creds = None
        
        # Check if token exists
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)
        
        # If no valid credentials, login
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_path):
                    logger.error(f"Credentials file not found at {self.credentials_path}")
                    logger.info("Please download OAuth credentials from Google Cloud Console")
                    return
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save credentials for next run
            with open(self.token_path, 'w') as token:
                token.write(creds.to_json())
        
        try:
            self.service = build('drive', 'v3', credentials=creds)
            logger.info("✅ Successfully authenticated with Google Drive")
        except Exception as e:
            logger.error(f"❌ Failed to build Drive service: {e}")
    
    def list_files(self, folder_id: Optional[str] = None, max_results: int = 100) -> List[Dict]:
        """
        List files in Google Drive
        Args:
            folder_id: Optional folder ID to list files from
            max_results: Maximum number of results to return
        Returns:
            List of file metadata dictionaries
        """
        if not self.service:
            logger.error("Service not initialized")
            return []
        
        try:
            query = f"'{folder_id}' in parents" if folder_id else None
            
            results = self.service.files().list(
                pageSize=max_results,
                q=query,
                fields="nextPageToken, files(id, name, mimeType, size, modifiedTime, parents)"
            ).execute()
            
            files = results.get('files', [])
            logger.info(f"Found {len(files)} files")
            return files
            
        except HttpError as error:
            logger.error(f"An error occurred: {error}")
            return []
    
    def download_file(self, file_id: str, destination_path: str) -> bool:
        """
        Download a file from Google Drive
        Args:
            file_id: Google Drive file ID
            destination_path: Local path to save file
        Returns:
            True if successful, False otherwise
        """
        if not self.service:
            logger.error("Service not initialized")
            return False
        
        try:
            request = self.service.files().get_media(fileId=file_id)
            
            # Create destination directory if needed
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            
            with io.FileIO(destination_path, 'wb') as fh:
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    if status:
                        logger.info(f"Download {int(status.progress() * 100)}%")
            
            logger.info(f"✅ Downloaded file to {destination_path}")
            return True
            
        except HttpError as error:
            logger.error(f"❌ Download failed: {error}")
            return False
    
    def upload_file(self, file_path: str, folder_id: Optional[str] = None, 
                    file_name: Optional[str] = None) -> Optional[str]:
        """
        Upload a file to Google Drive
        Args:
            file_path: Local file path to upload
            folder_id: Optional folder ID to upload to
            file_name: Optional custom name for the file
        Returns:
            File ID if successful, None otherwise
        """
        if not self.service:
            logger.error("Service not initialized")
            return None
        
        try:
            file_metadata = {
                'name': file_name or os.path.basename(file_path)
            }
            
            if folder_id:
                file_metadata['parents'] = [folder_id]
            
            media = MediaFileUpload(file_path, resumable=True)
            
            file = self.service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            
            logger.info(f"✅ Uploaded file with ID: {file.get('id')}")
            return file.get('id')
            
        except HttpError as error:
            logger.error(f"❌ Upload failed: {error}")
            return None
    
    def get_file_content(self, file_id: str) -> Optional[bytes]:
        """
        Get file content as bytes
        Args:
            file_id: Google Drive file ID
        Returns:
            File content as bytes, or None if failed
        """
        if not self.service:
            logger.error("Service not initialized")
            return None
        
        try:
            request = self.service.files().get_media(fileId=file_id)
            
            file_content = io.BytesIO()
            downloader = MediaIoBaseDownload(file_content, request)
            
            done = False
            while not done:
                status, done = downloader.next_chunk()
            
            return file_content.getvalue()
            
        except HttpError as error:
            logger.error(f"❌ Failed to get content: {error}")
            return None
    
    def get_file_content(self, file_id: str) -> str:
        """Get content of a specific file by ID"""
        try:
            if not self.service:
                self.authenticate()
            
            # Get file metadata first
            file_metadata = self.service.files().get(fileId=file_id, fields='mimeType,name').execute()
            mime_type = file_metadata.get('mimeType', '')
            
            # Handle Google Docs export
            if 'google-apps' in mime_type:
                if 'document' in mime_type:
                    export_mime = 'text/plain'
                elif 'spreadsheet' in mime_type:
                    export_mime = 'text/csv'
                elif 'presentation' in mime_type:
                    export_mime = 'text/plain'
                else:
                    return "Unsupported Google file type"
                
                content = self.service.files().export(fileId=file_id, mimeType=export_mime).execute()
                return content.decode('utf-8')
            else:
                # Regular file download
                content = self.service.files().get_media(fileId=file_id).execute()
                return content.decode('utf-8', errors='ignore')
                
        except Exception as e:
            self.logger.error(f"Error getting file content: {e}")
            return f"Error loading file: {str(e)}"
    
    def search_files(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search for files in Google Drive
        Args:
            query: Search query (e.g., "name contains 'bitcoin'")
            max_results: Maximum number of results
        Returns:
            List of matching files
        """
        if not self.service:
            logger.error("Service not initialized")
            return []
        
        try:
            results = self.service.files().list(
                pageSize=max_results,
                q=query,
                fields="files(id, name, mimeType, size, modifiedTime)"
            ).execute()
            
            files = results.get('files', [])
            logger.info(f"Search found {len(files)} files")
            return files
            
        except HttpError as error:
            logger.error(f"❌ Search failed: {error}")
            return []
    
    def create_folder(self, folder_name: str, parent_id: Optional[str] = None) -> Optional[str]:
        """
        Create a folder in Google Drive
        Args:
            folder_name: Name of the folder
            parent_id: Optional parent folder ID
        Returns:
            Folder ID if successful, None otherwise
        """
        if not self.service:
            logger.error("Service not initialized")
            return None
        
        try:
            file_metadata = {
                'name': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            
            if parent_id:
                file_metadata['parents'] = [parent_id]
            
            folder = self.service.files().create(
                body=file_metadata,
                fields='id'
            ).execute()
            
            logger.info(f"✅ Created folder with ID: {folder.get('id')}")
            return folder.get('id')
            
        except HttpError as error:
            logger.error(f"❌ Folder creation failed: {error}")
            return None
    
    def sync_to_local(self, output_dir: str = 'gdrive_sync', folder_id: Optional[str] = None):
        """
        Sync Google Drive files to local directory
        Args:
            output_dir: Local directory to sync files to
            folder_id: Optional folder ID to sync from
        """
        files = self.list_files(folder_id=folder_id, max_results=1000)
        
        os.makedirs(output_dir, exist_ok=True)
        
        for file in files:
            file_id = file.get('id')
            file_name = file.get('name')
            mime_type = file.get('mimeType')
            
            # Skip Google Workspace files (Docs, Sheets, etc.)
            if 'google-apps' in mime_type:
                logger.info(f"Skipping Google Workspace file: {file_name}")
                continue
            
            local_path = os.path.join(output_dir, file_name)
            logger.info(f"Syncing: {file_name}")
            
            self.download_file(file_id, local_path)

def main():
    """Demo usage of Google Drive backend"""
    print("🔗 Google Drive Backend Integration")
    print("=" * 60)
    
    # Initialize backend
    drive = GoogleDriveBackend()
    
    if not drive.service:
        print("❌ Failed to initialize Google Drive. Please set up credentials.")
        print("\nSteps to set up:")
        print("1. Go to Google Cloud Console")
        print("2. Create OAuth credentials")
        print("3. Download as 'credentials.json'")
        print("4. Place in project root")
        return
    
    # List files
    print("\n📂 Your Google Drive Files:")
    files = drive.list_files(max_results=20)
    
    for i, file in enumerate(files, 1):
        print(f"{i}. {file.get('name')} ({file.get('mimeType')})")
    
    # Search example
    print("\n🔍 Searching for Bitcoin-related files:")
    bitcoin_files = drive.search_files("name contains 'bitcoin'")
    for file in bitcoin_files:
        print(f"  - {file.get('name')}")
    
    print("\n✅ Google Drive backend ready!")
    print("Use GoogleDriveBackend() in your application to access files")

if __name__ == "__main__":
    main()
