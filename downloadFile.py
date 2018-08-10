# -*- coding: UTF-8 -*-
import main, sys, io


def download_File(file_id, file_path):
    """
      Download file
      Args:
        file_id: file id.
        file_path: Path where the file will be downloaded. 
    """
    files = main.drive_service.files()
    req = files.get_media(fileId=file_id)
    fh = io.FileIO(file_path, mode='wb')
    req.uri = req.uri.replace('alt=json', 'alt=media')
    downloader = main.MediaIoBaseDownload(fh, req, chunksize=1024*1024)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        if status:
            print("Download %d%%." % int(status.progress() * 100))

