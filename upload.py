
import os
import yaml
import pandas as pd

from azure.storage.blob import ContainerClient,BlobServiceClient

def load_config():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open(dir_root+ "/config.yaml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def get_files(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry

def upload(files, connecting_string, container_name):
    """Blob container class to manipulate azure storage container and  its blobs"""
    container_client = ContainerClient.from_connection_string(connecting_string, container_name)
    print("uploading files in progress...")


    for file in files:

        blob_client = container_client.get_blob_client(file.name)
        with open(file.path, "rb") as data:
            blob_client.upload_blob(data)
            print(f'{file.name} uploading to blob storage')
            # if we need to remove the files from source folder we user below lines#
            # os.remove(files)#
            # print(f'{file.name} removed from')#


config = load_config()
pict = get_files(config["source_folder"]+"/Pictures")
video = get_files(config["source_folder"]+"/Videos")
upload(pict,config["azure_storeage_connectionstring"],config["pictures_container_name"])
upload(video,config["azure_storeage_connectionstring"],config["video_container_name"])

