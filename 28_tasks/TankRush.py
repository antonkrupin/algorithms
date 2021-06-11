def TankRush(h1,w1,map1,h2,w2,map2):
    #h1, h2 - количество строк
    #w1, w2 - количество столбцов
    map1 = map1.split()
    map2 = map2.split()
    fullElementsArray = []
    if(h1 <= 0 or h2 <= 0 or w1 <= 0 or w2 <= 0):
        return False
    
    if(h2 > h1 or w2 > w1):
        return False
    else:
        for x in range(len(map1)):
            pointer = 0
            for y in range(len(map1[x])):
                if(len(map1[x][pointer:pointer+w2]) == w2):
                    element = map1[x][pointer:pointer+w2]
                    elementsArray = []
                    if(element == map2[0]):
                        elementsArray.append(element)
                        if(x+1 < len(map1)):
                            for z in range(x+1,len(map1)):
                                r = map1[z][pointer:pointer+w2]
                                elementsArray.append(r)
                                if(len(elementsArray) >= len(map2)):
                                    break
                        else:
                            if(len(elementsArray) < len(map2)):
                                for z in range(x+1,len(map2)):
                                    r = map1[z][pointer:pointer+w2]
                                    elementsArray.append(r)
                                
                        if(len(elementsArray) != 0):
                            fullElementsArray.append(elementsArray)
                    
                pointer += 1
        for x in range(len(fullElementsArray)):
            print(fullElementsArray[x])
        if(map2 in fullElementsArray):
            return True
        else:
            return False
