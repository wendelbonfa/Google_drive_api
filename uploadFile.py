# -*- coding: UTF-8 -*-
import main


def upload_File(file_name, file_path, mimetype, id_Folder=None):
    """
      Upload file from drive
      Args:
        file_name: Name file to be uploaded.
        file_path: Path file to be uploaded.
        # for accept type look under link
        # https://developers.google.com/drive/api/v3/integrate-open
        mimetype: Type file to be uploaded. 
        id_Folder: if possible upload in specific folder  
 
    """
    if id_Folder:
        file_metadata = {
            'name': file_name,
            'parents': [id_Folder]
        }
    else:
        file_metadata = {'name': file_name}
    media = main.MediaFileUpload(file_path, mimetype=mimetype, resumable=True)
    file = main.drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
