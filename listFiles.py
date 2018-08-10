# -*- coding: UTF-8 -*-
import main


def list_Files(size):
    """
      list of files passed as parameter.
      Args:
        size: Amount show list.        
      Return:
        list files with size amount.
    """
    results = main.drive_service.files().list(pageSize=size, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        return items


