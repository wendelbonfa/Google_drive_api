# -*- coding: UTF-8 -*-
from main import *


def delete_file(file_id):
    """
      Permanently delete a file, skipping the trash.
      Args:
        file_id: ID of the file to delete.
    """
    try:
      main.drive_service.files().delete(fileId=file_id).execute()
    except:
      print('An error occurred:')


