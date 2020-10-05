from generateFiles import generateFiles as gf

gf(10)

def handlingFiles(fileNumber1, fileNumber2):
    sumNumbers = 0
    filePath1 = str(fileNumber1) + '.txt'
    filePath2 = str(fileNumber2) + '.txt'

    f1 = open(filePath1)
    f2 = open(filePath2)

    def checkFile(opendFile):
        counter = 0
        for s in opendFile:
            counter += 1
            try:
                intLine = int(s.rstrip())
            except Exception:
                print ('The file is corrupted')

        if counter != 3:
            return 'Файл не полный'

    #checkFile(f1)
    #checkFile(f2)
    
    for s in f1:
        sumNumbers += int(s.rstrip())
    f1.close()
    
    for s in f2:
        sumNumbers += int(s.rstrip())

    return sumNumbers

if __name__ == "__main__":
    print(handlingFiles(2,5))
#print(handlingFiles(2,5))