import os
import subprocess
import shutil
import psutil
import platform

class File:
    def LoadFileData(self, directory, onefile=False):
        dir = os.listdir(directory)
        responce = []
        if onefile == False:
            for file in dir:
                filedir = f'{directory}/{file}'
                config = {
                    "name": file,
                    "localDir": filedir,
                    "fileExt": filedir.split('.').reverse()[0],
                    "fileSize": os.path.getsize(filedir),
                    "LastModified": os.path.getmtime(filedir),
                    "LastAccesed": os.path.getatime(filedir),
                }
                responce.insert(config)
            return responce
        elif onefile == True:
            config = {
                "name": file,
                "localDir":directory.split('/').reverse()[0],
                "fileExt": directory.split('.').reverse()[0],
                "fileSize": os.path.getsize(directory),
                "LastModified": os.path.getmtime(directory),
                "LastAccesed": os.path.getatime(directory),
            }
            return config
        else: raise 'onefile can only be set to True or False'