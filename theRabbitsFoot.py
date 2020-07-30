def TheRabbitsFoot(string, flag):
    lenString = len(string)
    #квардратный корень из длинны строки без пробелов
    sqrtLen = lenString**(1/2)
    #число столбцов
    n = round(sqrtLen)
    #число строк
    m = round(sqrtLen-0.5)
    
    criptedString = []
    
    criptedStringFull = ""
    
    if(m*n < lenString):
        m = m+1
    if(flag):
        string = string.strip().replace(' ', '')
        pointer = 0
        for x in range(m):
            subString = string[pointer:pointer+n]
            if(len(subString) < n):
                zeroFillSize = n - len(subString)
                subString = subString + '0' * zeroFillSize
                criptedString.append(subString)
                pointer = pointer + n
            else:
                criptedString.append(subString)
                pointer = pointer + n
        
        for i in range(len(criptedString[0])):
            testLen = len(criptedString[i])
            test = ""
            for j in range(testLen):
                if(criptedString[j][i] != '0'):
                    test = test + criptedString[j][i]
                    
            criptedStringFull = criptedStringFull + test + ' '
            
        return criptedStringFull
    else:
        print(string)
        splitString = string.split()
        criptedString = []
        criptedStringFull = ""
        maxLength = len(splitString[0])
        
        for x in range(len(splitString)):
            if(len(splitString[x]) < maxLength):
                subString = splitString[x] + '0'
                criptedString.append(subString)
            else:
                criptedString.append(splitString[x])
        
        for i in range(len(criptedString)):
            for j in range(len(criptedString[i])):
                if(criptedString[j][i] != 0):
                    criptedStringFull = criptedStringFull + criptedString[j][i]
                else:
                    criptedStringFull = criptedStringFull
        
        return criptedStringFull.replace('0','')