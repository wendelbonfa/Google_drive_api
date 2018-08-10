# -*- coding: UTF-8 -*-
from main import *


def search_File(size, file_name):
    """
      Search file with name passed
      Args:
        size: Amount show list.
        file_name: Name to be located. 
      Return:
        list files with size amount.      
    """
    locate_list = []
    results = drive_service.files().list(pageSize=size, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        for item in items:
            if item['name'] == file_name:
                locate_list.append(item)
        return locate_list


