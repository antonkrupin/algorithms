def checkSubString(string, subString):
    for i in range(len(string)):
        counter = 0
        if string[i] == subString[0]:
            counter += 1
            for j in range(1,len(subString)):
                if i + j < len(string):
                    if string[i + j] == subString[j]:
                        counter += 1
        if counter == len(subString):
            return True
    return False
