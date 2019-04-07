#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
    
import auth
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def download_file(file_id, file_path):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False: 
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
        
    with io.open(file_path, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())
#https://drive.google.com/file/d/1ALXmFWrnaV7vhCDMPW2N4sPudTsqpjr-/view?usp=sharing
download_file('1ALXmFWrnaV7vhCDMPW2N4sPudTsqpjr-', 'nicholascage.jpg')