import os

def getDirectoryFilesAndFolders(mainDirectoryPath):
    folders = []
    files = []
    
    if os.path.isdir(mainDirectoryPath):
        for i in os.walk(mainDirectoryPath):
            if len(i[1]) != 0:
                for j in i[1]:
                    folders.append(j)
            if len(i[2]) != 0:
                for j in i[2]:
                    files.append(j)
        return [folders, files, 1]
    else:
        return [folders, files, -1]


def deleteDirectory(mainDirectoryPath):
    mainDirectoryName = os.path.split(mainDirectoryPath)[1]

    for i in os.walk(mainDirectoryPath):
        splitedDirectoryPath = i[0].split('\\')[-1]
            
        if splitedDirectoryPath == mainDirectoryName:
            if len(i[1]) != 0:
                return -1
            else:
                for y in i[2]:
                    filePath = i[0] + '\\' + y
                    os.remove(filePath)
                os.rmdir(mainDirectoryPath)
                return 1

