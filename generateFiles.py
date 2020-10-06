from random import randint
    
def generateFiles(numberOfFiles):
    for x in range(1,numberOfFiles + 1):
        fileName = str(x)+'.txt'
        f = open(fileName, 'wt')
        for i in range(3):
            number = str(randint(0,100)) + '\n'
            f.write(number)
        f.close()

def checkFile(filePath):
    f = open(filePath)
    counter = 0

    for string in f:
        try:
            int(string)
        except Exception:
            continue
        else:
            counter += 1

    f.close()
    
    if counter == 3:
        return True
    else:
        return False