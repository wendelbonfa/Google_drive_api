# -*- coding: UTF-8 -*-
import main


def createFolder(name):
    """
      Create folder in Google Drive.
      Args:
        name: Name used in folder created.
    """
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = main.drive_service.files().create(body=file_metadata, fields='id').execute()



