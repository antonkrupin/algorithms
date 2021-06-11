def BalancedParentheses(count):
    
    string = []
    for x in range(count*2):
        string.append(0)
    
    def addParent(arrayList, leftRem, rightRem, string, count):
        if (leftRem < 0 or rightRem < leftRem):
            return
        
        if (leftRem == 0 and rightRem == 0):
            s = string.copy()
            arrayList.append(s)
        else:
            if (leftRem > 0):
                string[count] = '('
                addParent(arrayList, leftRem - 1, rightRem, string, count + 1) 
            if (rightRem > leftRem):
                string[count] = ')'
                addParent(arrayList, leftRem, rightRem - 1, string, count + 1)

    arrayList = []
    addParent(arrayList, count, count, string, 0)
    
    
    for x in range(len(arrayList)):
        arrayList[x] = ''.join(arrayList[x])

    finalList = ' '.join(arrayList)

    return finalList
