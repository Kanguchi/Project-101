import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for name in files:
                local_path = os.path.join(root, name)
                print(local_path)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

            with open(local_path, 'rb') as f:
                dbx.files_upload(f.read(), dropbox_path, mode = dropbox.files.WriteMode.overwrite)
            
def main():
    access_token = 'AEVrYIouAOcAAAAAAAAAAclTtMfM4NMgRXMUAou1S0ot_Vw-7bp_JaI-rwsoKGsL'
    transferData = TransferData(access_token)

    file_from = input("Filepath Transfer : ")
    file_to = input("Enter the full path to trandsfer to dropbox : ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()