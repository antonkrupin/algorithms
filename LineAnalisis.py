def LineAnalysis(analyseString):
    pattern = ""
    if(analyseString[0] == '*' and analyseString[-1] == '*'):
        for x in range(1,len(analyseString)):
            if(analyseString[x] == '*'):
                pattern = analyseString[0:x+1]
                break
            
        pointer = 0
        p = len(pattern)
        
        for x in range(len(analyseString)):
            patternSlice = analyseString[pointer:pointer+p]
            print(patternSlice)
            if(len(patternSlice) == p):
                if(patternSlice != pattern):
                    return False
            else:
                return False
            pointer += p-1
        return True
    else:
        return False
print(LineAnalysis('*..........*..........*'))
