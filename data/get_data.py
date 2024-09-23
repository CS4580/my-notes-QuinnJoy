"""Download data from our server
"""
#import requests
import zipfile
import shutil
import os, sys

SERVER_URL = 'http://icarus.cs.weber.edu/~hvalle/cs4580/data/'

def download_file(url,file_name):
    #TODO: Download to pwd
    full_url = url + file_name
    response = response.get(full_url)

    pass


def unzip_file(file_name):
    #TODO: Unzip file check extension, if it is zip 
    #Call unzip_file()
    #unzip_file(data01)
    pass


def main():
    """Driven Function
    """
    data = 'pandas01Data.zip'
    download_file(SERVER_URL,data)
    unzip_file(data)


if __name__ == "__main__":
    main()
