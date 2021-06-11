def LineAnalysis(analyseString):
    pattern = ""
    slicedString = []
    if(analyseString[0] == '*' and analyseString[-1] == '*'):
        for x in range(1,len(analyseString)):
            if(analyseString[x] == '*'):
                pattern = analyseString[0:x+1]
                break
            
        pointer = 0
        p = len(pattern)
        
        for x in range(len(analyseString)):
            patternSlice = analyseString[pointer:pointer+p]
            
            if(patternSlice != '' and len(patternSlice) == p):
                slicedString.append(patternSlice)
            pointer += p-1
        
        print(slicedString)
        for x in range(len(slicedString)):
            if(slicedString[x] != pattern):
                return False
                break
        return True
        
    else:
        return False
