# -*- coding: UTF-8 -*-
import createFolder
import uploadFile
import deleteFile
import downloadFile
import searchFile
import listFiles

"""
  Test all function google
"""
createFolder.createFolder('teste_hi')
folder_id = searchFile.search_File(1, 'teste_hi')
# for accept type look under link
# https://developers.google.com/drive/api/v3/integrate-open
uploadFile.upload_File('logo.png', 'logo.png', 'image/png', str(folder_id[0]['id']))
items = listFiles.list_Files(100)
for item in items:
    print(u'{0} ({1})'.format(item['name'], item['id']))
print("Look your google drive")
main.os.system("pause")
file_id = searchFile.search_File(1, 'logo.png')
downloadFile.download_File(str(file_id[0]['id']), 'C:\\Users\\Public\\Desktop\\logo.png')
deleteFile.delete_file(str(file_id[0]['id']))
deleteFile.delete_file(str(folder_id[0]['id']))
print("Look your Desktop")
