fullString = []
changeList = []
undoCounter = 0

def BastShoe(string):
    operationNumber = string[0:1]
    endOfLine = string[1:].strip()
    
    if(operationNumber == '1'):
        if(len(fullString) == 0):
            fullString.append(endOfLine)
            changeList.append([operationNumber,endOfLine])
        else:
            fullString[0] = fullString[0] + endOfLine
            changeList.append([operationNumber,endOfLine])
    
    if(operationNumber == '2'):
        if(int(endOfLine) >= len(fullString[0])):
            changeList.append([operationNumber,fullString[0]])
            fullString[0] = ''
        else:
            removed = fullString[0][-int(endOfLine):]
            changeList.append([operationNumber,removed])
            fullString[0] = fullString[0][0:-int(endOfLine)]
    
    if(operationNumber == '3'):
        if(int(endOfLine) > len(fullString[0])):
            return ''
        else:
            return fullString[0][int(endOfLine)]
    
    if(operationNumber == '4'):
        for x in reversed(range(len(changeList))):
            if(changeList[x][0] == '2'):
                undoString = fullString[0] + changeList[x][1]
                fullString[0] = undoString
                changeList.pop()
                return fullString[0]
            if(changeList[x][0] == '1'):
                undoString = fullString[0][:len(fullString[0])-len(changeList[x][1])]
                fullString[0] = undoString
                changeList.pop()
                return fullString[0]
                
    #print(changeList)
    return fullString[0]
    
print(BastShoe('1 Привет'))
print(BastShoe('1 , Мир!'))
print(BastShoe('1  ++'))
print(BastShoe('2 2'))
print(BastShoe('1 Приветище'))
print(BastShoe('4'))
print(BastShoe('1 55555'))
print(BastShoe('4'))
print(BastShoe('4'))
