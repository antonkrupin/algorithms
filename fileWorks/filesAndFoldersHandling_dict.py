import os

folders = []

def getDirectoryFilesAndFolders(mainDirectoryPath):
    
    mainDirectoryName = os.path.split(mainDirectoryPath)[1]

    if os.path.isdir(mainDirectoryPath):
        directoryTreeFolders = {
            'title': 'Folders in directory'
        }
        directoryTreeFiles = {
            'title': 'Files in directory'
        }

        for i in os.walk(mainDirectoryPath):
            
            splitedDirectoryPath = i[0].split('\\')[-1]
            
            if splitedDirectoryPath == mainDirectoryName:
                directoryTreeFolders[mainDirectoryName] = i[1]
                directoryTreeFiles[mainDirectoryName] = i[2]
            
            if splitedDirectoryPath in directoryTreeFolders[mainDirectoryName]:
                directoryTreeFolders[splitedDirectoryPath] = i[1]
                directoryTreeFiles[splitedDirectoryPath] = i[2]
            else:
                directoryTreeFolders[splitedDirectoryPath] = i[1]
                directoryTreeFiles[splitedDirectoryPath] = i[2]
           
        def returnDict(dictionary):
            for key in dictionary:
                if key != 'title':
                    print(f'{key}: {dictionary[key]}')
                else:
                    print(f'{dictionary[key]}:')
                    print()
            print('\n')
        
        return returnDict(directoryTreeFolders), returnDict(directoryTreeFiles)
    else:
        return -1


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
            

#deleteDirectory('E:\\algorithms-master\\fileworks')
getDirectoryFilesAndFolders('E:\\algorithms-master\\fileworks')
