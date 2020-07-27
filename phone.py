def PatternUnlock(n, hits):
    length = 0
    b = 2
    p = 2**(1./b)
    
    longSideSequence = [[1,5],[5,1],[1,8],[8,1],[2,4],
                        [4,2],[2,6],[6,2],[2,7],[7,2],
                        [2,9],[9,2],[3,5],[5,3],[3,8],[8,3]]
    
    for x in range(len(hits)-1):
        m = []
        m.append(hits[x])
        m.append(hits[x+1])
        
        if(m in longSideSequence):
            length = length + p
        else:
            if(m[0] == m[1]):
                length = length + 0
            else:
                length = length + 1
    
    lengthString = str(round(length,5))
    
    formatedString = ""

    for x in range(len(lengthString)):
        if(lengthString[x] != '.' and lengthString[x] != '0'):
            formatedString = formatedString + lengthString[x]
    
    return formatedString