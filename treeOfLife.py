def TreeOfLife(treeHeight, treeWidth, years, tree):
    
    for x in range(len(tree)):
        replacedString = tree[x].replace('+','1')
        replacedString = replacedString.replace('.','0')
        tree[x] = replacedString
    
    yearsCounter = 0
    
    while(yearsCounter < years):
        yearsCounter += 1
        
        #нечетный год
        if(yearsCounter%2 != 0):
            for x in range(len(tree)):
                treeString = list(tree[x])
                for y in range(len(treeString)):
                    treeChar = treeString[y]
                    if(treeChar != '.'):
                        treeChar = int(treeChar)
                        treeChar += 1
                        treeChar = str(treeChar)
                        treeString[y] = treeChar
                    if(treeChar == '.'):
                        treeChar = '1'
                        treeString[y] = treeChar
                tree[x] = treeString
                
        #четный год
        if(yearsCounter%2 == 0):
            deadCoords = []
            for x in range(len(tree)):
                treeString = list(tree[x])
                for y in range(len(treeString)):
                    treeChar = treeString[y]
                    if(treeChar != '.'):
                        treeChar = int(treeChar)
                        treeChar += 1
                        treeChar = str(treeChar)
                        treeString[y] = treeChar
                    if(treeChar == '.'):
                        treeChar = '1'
                        treeString[y] = treeChar
                tree[x] = treeString
            
            for x in range(len(tree)):
                treeString = tree[x]
                for y in range(len(treeString)):
                    if(treeString[y] != '.' and treeString[y] != '.3'):
                        treeString[y] = int(treeString[y])
                        if(treeString[y] >= 3):
                            treeString[y] = '.'
                            deadCoords.append([x,y])
                            
            for x in range(len(deadCoords)):
                if(deadCoords[x][0] == 0):
                    coordX = deadCoords[x][0]
                    coordY = deadCoords[x][1]
                    tree[coordX+1][coordY] = '.'
                elif(deadCoords[x][0] == len(tree)-1):
                    coordX = deadCoords[x][0]
                    coordY = deadCoords[x][1]
                    tree[coordX-1][coordY] = '.'
                else:
                    coordX = deadCoords[x][0]
                    coordY = deadCoords[x][1]
                    tree[coordX+1][coordY] = '.'
                    tree[coordX-1][coordY] = '.'
                    
                if(deadCoords[x][1] == 0):
                    coordX = deadCoords[x][0]
                    coordY = deadCoords[x][1]
                    tree[coordX][coordY+1] = '.'
                elif(deadCoords[x][1] == len(tree[0])-1):
                    coordX = deadCoords[x][0]
                    coordY = deadCoords[x][1]
                    tree[coordX][coordY-1] = '.'
                else:
                    coordX = deadCoords[x][0]
                    coordY = deadCoords[x][1]
                    tree[coordX][coordY+1] = '.'
                    tree[coordX][coordY-1] = '.'
    
    for x in range(len(tree)):
        for y in range(len(tree[x])):
            if(tree[x][y] != '.'):
                tree[x][y] = '+'
                
    for x in range(len(tree)):
        string = ''
        for y in range(len(tree[x])):
            string = string + str(tree[x][y])
        tree[x] = string
        
    return tree
