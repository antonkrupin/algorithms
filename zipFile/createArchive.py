import os
from zipfile import ZipFile

def findFilesAndCreateArchive(archiveName, fileExtension):
    isFilesInDirectory = False
    directory = os.getcwd()
    
    if fileExtension[0] != '.':
        fileExtension = '.' + fileExtension
        
    for i in os.walk(directory):    
        for file in i[2]:
            if file[-len(fileExtension):] == fileExtension:
                if isFilesInDirectory == False:
                    isFilesInDirectory = True
                    zf = ZipFile(archiveName, mode='w')
                    if i[0] == directory and file not in zf.namelist():
                        zf.write(file)
                else:
                    if i[0] == directory and file not in zf.namelist():
                        zf.write(file)   
    
    if isFilesInDirectory:
        zf.close()
        return 1
    else:
        return -1            
                