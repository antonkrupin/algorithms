fullString = ['']
changeList = []

undoCounter = []
undoCounter.append(True)

redoCounter = []
undoChanges = []

def BastShoe(string):
    operationNumber = string[0:1]
    if((operationNumber != '1') and (operationNumber != '2')
        and (operationNumber != '3') and (operationNumber != '4')
        and (operationNumber != '5')):
            return fullString[0]
    else:
        if(len(string) != 1):
            if(string[2] == '.' or 
                string[2] == ',' or
                string[2] == '-'):
                endOfLine = string[1:].strip()
            else:
                endOfLine = string[1:].strip()
        
        if(operationNumber == '1'):
            undoCounter[0] = True
            redoCounter.clear()
            if(len(undoChanges) != 0):
                if(len(changeList) == 1):
                    undoChangesCopy = undoChanges.copy()
                    changeList.insert(0,undoChangesCopy)
                else:
                    undoChangesCopy = undoChanges.copy()
                    changeList.insert(len(changeList)-1,undoChangesCopy)
                undoChanges.clear()
                
            if(len(fullString) == 0):
                fullString.append(endOfLine)
                changeList.append([operationNumber,endOfLine])
            else:
                fullString[0] = fullString[0] + endOfLine
                changeList.append([operationNumber,endOfLine])
        
        if(operationNumber == '2'):
            undoCounter[0] = True
            redoCounter.clear()
            
            if(len(undoChanges) != 0):
                if(len(changeList) == 1):
                    undoChangesCopy = undoChanges.copy()
                    changeList.insert(0,undoChangesCopy)
                else:
                    undoChangesCopy = undoChanges.copy()
                    changeList.insert(len(changeList)-1,undoChangesCopy)
                undoChanges.clear()
                
            if(int(endOfLine) >= len(fullString[0])):
                changeList.append([operationNumber,fullString[0]])
                fullString[0] = ''
            else:
                removed = fullString[0][-int(endOfLine):]
                changeList.append([operationNumber,removed])
                fullString[0] = fullString[0][0:-int(endOfLine)]
        
        if(operationNumber == '3'):
            undoCounter[0] = True
            if(int(endOfLine) < 0 or int(endOfLine) > len(fullString[0])):
                return ''
            else:
                return fullString[0][int(endOfLine)]
        
        if(operationNumber == '4'):
            if(undoCounter[0] == True):
                changeList.append([operationNumber,'undo'])
                undoCounter[0] = False
                
            for x in reversed(range(len(changeList)-1)):
                if(changeList[x][1] != 'undo'):
                    t = changeList[x].copy()
                    undoChanges.append(t)
                    changeList.pop(-2)
                else:
                    break
                
            for x in range(len(undoChanges)):
                if(undoChanges[x][0][0] == '1' and not 'u' in undoChanges[x][0]):
                    undoString = fullString[0][:len(fullString[0])-len(undoChanges[x][1])]
                    fullString[0] = undoString
                    undoChanges[x][0] = undoChanges[x][0][0] + 'u'
                    return fullString[0]
                
                if(undoChanges[x][0][0] == '2' and not 'u' in undoChanges[x][0]):
                    undoString = fullString[0] + undoChanges[x][1]
                    fullString[0] = undoString
                    undoChanges[x][0] = undoChanges[x][0][0] + 'u'
                    return fullString[0]
                
        if(operationNumber == '5'):
            if(len(undoChanges) > 0):
                for x in reversed(range(len(undoChanges))):
                    if(undoChanges[x][0][0] == '1' and 'u' in undoChanges[x][0]):
                        redoString = fullString[0] + undoChanges[x][1]
                        fullString[0] = redoString
                        undoChanges[x][0] = undoChanges[x][0][0] + 'r'
                        return fullString[0]
                    if(undoChanges[x][0][0] == '2' and 'u' in undoChanges[x][0]):
                        redoString = fullString[0][:len(fullString[0])-len(undoChanges[x][1])]
                        fullString[0] = redoString
                        undoChanges[x][0] = undoChanges[x][0][0] + 'r'
                        return fullString[0]
            else:
                return fullString[0]
                    
        return fullString[0]
