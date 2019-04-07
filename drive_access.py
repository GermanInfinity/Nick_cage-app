#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 8:02:12 2019

@author: Akwarandu Ugo Nwachuku
Description: This module is responsible for gaining access to the google
             drive API and downloading the shared image. 
"""
from __future__ import print_function
import httplib2
import os, io
import auth

from my_image_processing import apply_makeup

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
        print("This much of Nicholas Cage has been downloaded: %d%%." % int(status.progress() * 100))
        
    with io.open(file_path, 'wb') as f:
        fh.seek(0)
        f.write(fh.read())

download_file('1ALXmFWrnaV7vhCDMPW2N4sPudTsqpjr-', 'nicholascage.jpg')

apply_makeup('nicholascage.jpg')
