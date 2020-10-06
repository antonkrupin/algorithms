from generateFiles import generateFiles as gf
from generateFiles import checkFile as cf

gf(10)

def handlingFiles(fileNumber1, fileNumber2):
    sumNumbers = 0

    filePath1 = str(fileNumber1) + '.txt'
    filePath2 = str(fileNumber2) + '.txt'
   
    if cf(filePath1) and cf(filePath2):
        f1 = open(filePath1)
        f2 = open(filePath2)

        for s in f1:
            sumNumbers += int(s.rstrip())
        f1.close()
        
        for s in f2:
            sumNumbers += int(s.rstrip())
        f2.close()

        return sumNumbers
    else:
        return 'Файл или файлы повреждены (некорректно заполнены)'
        
if __name__ == "__main__":
    print(handlingFiles(2,5))
