
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json

class GoogleDirectory:
    def __init__(self,**kwargs):
        self.scopes = ['https://www.googleapis.com/auth/admin.directory.user','https://www.googleapis.com/auth/admin.directory.group']

        self.creds = None

        self.token_path = kwargs.get('token','~/.googledirectory/token.pickle')
        # if you are running locally and need to generate a fresh token, 
        # you must provide a creds path for auth
        self.creds_path = kwargs.get('creds','~/.googledirectory/credentials.json')

        self.token_path = os.path.expanduser(self.token_path)
        self.creds_path = os.path.expanduser(self.creds_path)

        if self.token_path and os.path.exists(self.token_path):
            with open(self.token_path, 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            self.refresh_creds()

        self.service = build('admin', 'directory_v1', credentials=self.creds)

    def refresh_creds(self):
        if self.creds and self.creds.expired and self.creds.refresh_token:
            self.creds.refresh(Request())
            self.save_creds()
            return
        if not os.path.exists(self.creds_path):
            raise Exception("""
                            Error: To generate a new session token you must specify a valid google creds file. 
                            You can download a creds file by following the instructions here: 
                            https://developers.google.com/admin-sdk/directory/v1/quickstart/python
                            """)
        if not os.path.exists(os.path.dirname(self.token_path)):
            os.makedirs(os.path.dirname(self.token_path))
        flow = InstalledAppFlow.from_client_secrets_file(self.creds_path, self.scopes)
        self.creds = flow.run_local_server(port=0)
        self.save_creds()
    def save_creds(self):
        with open(self.token_path, 'wb') as token:
            pickle.dump(self.creds, token)
    def add_member(self,group,email):
        try:
            self.service.members().insert(groupKey=group, body={'email': email,'role':'MEMBER'}).execute()
        except Exception as e:
            print("Could not add member: {}".format(str(e)))
    def remove_member(self,group,email):
        try:
            self.service.members().delete(groupKey=group,memberKey=email).execute()
        except Exception as e:
            print("Could not remove member: {}".format(str(e)))
    def get_all_groups(self):
        results = self.service.groups().list(customer='my_customer').execute()
        return [ x['email'] for x in results['groups'] ]
    def list_group_members(self,group):
        results = self.service.members().list(groupKey=group).execute()
        return [ x['email'] for x in results['members'] ]
    def create_group(self,group):
        results = self.service.groups().insert(body={'email': group}).execute()
        return results


