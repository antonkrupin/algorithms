fullString = []
changeList = []
undoCounter = []
undoCounter.append(True)

def BastShoe(string):
    operationNumber = string[0:1]
    endOfLine = string[1:].strip()
    
    if(operationNumber == '1'):
        undoCounter[0] = True
        if(len(fullString) == 0):
            fullString.append(endOfLine)
            changeList.append([operationNumber,endOfLine])
        else:
            fullString[0] = fullString[0] + endOfLine
            changeList.append([operationNumber,endOfLine])
    
    if(operationNumber == '2'):
        undoCounter[0] = True
        if(int(endOfLine) >= len(fullString[0])):
            changeList.append([operationNumber,fullString[0]])
            fullString[0] = ''
        else:
            removed = fullString[0][-int(endOfLine):]
            changeList.append([operationNumber,removed])
            fullString[0] = fullString[0][0:-int(endOfLine)]
    
    if(operationNumber == '3'):
        undoCounter[0] = True
        if(int(endOfLine) > len(fullString[0])):
            return ''
        else:
            return fullString[0][int(endOfLine)]
    
    if(operationNumber == '4'):
        if(undoCounter[0] == True):
            changeList.append([operationNumber,'undo'])
            undoCounter[0] = False
            
        for x in reversed(range(len(changeList)-1)):
            if(changeList[x][1] != 'undo'):
                if(changeList[x][0] == '2'):
                    undoString = fullString[0] + changeList[x][1]
                    fullString[0] = undoString
                    changeList.pop(-2)
                    return fullString[0]
                if(changeList[x][0] == '1'):
                    undoString = fullString[0][:len(fullString[0])-len(changeList[x][1])]
                    fullString[0] = undoString
                    changeList.pop(-2)
                    return fullString[0]
            else:
                break
    
    #print(changeList)
    return fullString[0]
 
print(BastShoe('1 Привет'))
print(BastShoe('1 , Мир!'))
print(BastShoe('1  ++'))
print(BastShoe('2 2'))
print(BastShoe('1 Приветище'))
print(BastShoe('4'))
print(BastShoe('1 Доброе утро!'))
print(BastShoe('2 2'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('4'))
print(BastShoe('1 !!!'))
