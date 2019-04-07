#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:28:58 2019

@author: ugoslight
"""
#https://drive.google.com/drive/folders/1DPyuH3mkZR0V3MTxOjb9ADkCKGUl0GDE

from apiclient import errors
# ...




def download_file(service, file_id, local_fd):
    request = service.files().get_media(fileId=file_id)
    media_request = http.MediaIoBaseDownload(local_fd, request)
    
    
def main():
    download_file(GET, '1DPyuH3mkZR0V3MTxOjb9ADkCKGUl0GDE', '/Desktop')

if __name__ == '__main__':
    main()
    
    
    
def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')`1
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():

    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    results = service.files().list(
        pageSize=10,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))

if __name__ == '__main__':
    main()
    
    
"""
Created on Fri Apr  5 21:48:17 2019

@author: Akwarandu Ugo Nwachuku
Description: 
    

   
import requests
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

site_request = requests.get('https://www.google.com' )

file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
request = drive_service.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print ("Download %d%%." % int(status.progress() * 100))

from oauth2client.client import flow_from_clientsecrets

if __name__ == '__main__':
    flow = client.flow_from_clientsecrets(
            'K-O3ql-0x6yHzxrKCJzvsmBU',
            scope='https://www.googleapis.com/auth/drive.readonly',
            redirect_uri='urn:ietf:wg:oauth:2.0:oob')
    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open(auth_uri)
    print(auth_uri)
    
"""