def MatrixTurn(matrix, matrixHeight, matrixLength, turns):
    martixArray = []
    
    if(matrixHeight >= matrixLength):
        numberOfCircles = matrixLength // 2
    else:
        numberOfCircles = matrixHeight // 2
    
    for x in range(len(matrix)):
        martixArray.append(list(matrix[x]))
    turnCounter = 0
    
    while(turnCounter < turns):
        i = 0
        while(i < numberOfCircles):
            for x in range(0 + i, len(martixArray)-i):
                if(x - i == 0):
                    nextFirstElement = martixArray[x+1][i]
                    martixArray[x].insert(i,nextFirstElement)
                elif(x < len(martixArray)-1-i and x - i != 0):
                    nextFirstElement = martixArray[x+1][i]
                    martixArray[x].pop(i)
                    martixArray[x].insert(i,nextFirstElement)
                    prevLastElement = martixArray[x-1][-(i+1)]
                    martixArray[x-1].pop(-(i+1))
                    martixArray[x].insert(-(i+1),prevLastElement)
                else:
                    if(i == 0):
                        martixArray[x].pop(i)
                        prevLastElement = martixArray[x-1][-(i+1)]
                        martixArray[x].append(prevLastElement)
                        martixArray[x-1].pop(-(i+1))
                    else:
                        martixArray[x].pop(i)
                        prevLastElement = martixArray[x-1][-(i+1)]
                        martixArray[x].insert(-i,prevLastElement)
                        martixArray[x-1].pop(-(i+1))
            i += 1
        turnCounter += 1
    
    for x in range(len(martixArray)):
        martixArray[x] = ''.join(martixArray[x])

    return martixArray   
