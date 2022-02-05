import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root, fileName)
                dropbox_path = os.path.join(file_to, fileName)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BBdhU5xk5K2CR7F8rgSCk2S0c_iYOYWKv4QDCrXcIj2Eqea9DP_TUQDIAc03mAwR_qtP_fvHfhX6Y1YNuMkyPHjXz_2ItnXH5qTi9qTlB63fivbmW8LcHTykyMzGMoJOO90kux0'
    transferData = TransferData(access_token)

    file_from = input("Enter the path you want to backup - ")
    file_to = input("Enter the dropbox path you want to create backup - ")

    transferData.upload_file(file_from, file_to)
    print("Backup has been created :) ")

main()