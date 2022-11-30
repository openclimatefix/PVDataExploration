# Libraries
import os
import sys
import random
from datetime import datetime, date, timedelta
from typing import Dict, List, Tuple, Union
from pathlib import Path
import requests
import zipfile
import io

def find_files(
    filename: str  = None, 
    search_path:str = None,
    print_bool: bool = False
    )-> None:
    """
    Find any file and returns the filename and its path
    Args:
    filename = filename to be searched for 
    search_path = directory of the Searching path
    """
    dir_path = None
    for root, dir, files in os.walk(search_path):
        if filename in files:
            dir_path = Path(os.path.join(root, filename)).parent.as_posix()
    if dir_path not in sys.path:
        sys.path.append(dir_path)
    file_path = Path(os.path.join(dir_path, filename)).as_posix()
    if print_bool:
        print("\nPath to your file is :\n", file_path)
        print("\nDirectory of that file is:\n", dir_path)
        return dir_path, file_path
    else:
        return dir_path, file_path

def create_dir(
    working_dir:str = None,
    dir_name:str = None
    )->None:
    """
    A function to create a directory and attach that 
    to the working directory
    Args:
    working_dir = Wokrking directory
    dir_name = Name of the directory needed to be created
    """
    dir = os.path.join(Path(working_dir).as_posix(), dir_name)
    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok = True)
    return dir

def download_zip_url(
    zip_file_url: str = None,
    path_to_save:str = None
    )->None:
    """
    A function to download a zip file from the url
    and save it in a specified folder
    Args:
    zip_file_url = url of the zip file
    path_to_save = A path of the folder to which
    the zip files are going to be extracted to
    """
    #Downloading and extracting
    print("\nDownloading the zip files...........\n")
    with requests.get(zip_file_url, stream = True) as r:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        print("\nDownload complete.......................\n")
        print("\nBegin Extracting the files in zip..........\n")
        z.extractall(path = path_to_save)
        print("\nExtraction complete............\n")

