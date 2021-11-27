from os import access
import dropbox

class transferData():
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '0iCq0KczEssAAAAAAAAAAUXkwDW8M7ItNZtEnIvMmAjjiB9Q3pbtPyBPjFFewsBl'
    transfer_data = transferData(access_token)

    file_from = input("Enter The FIle Path To Tranfer: ")
    file_to = input("Enter The Full Path To Upload To Dropbox: ")

    transfer_data.upload_file(file_from, file_to)
    print("File Has Been Uploaded Successfully")

main()