def TankRush(h1,w1,map1,h2,w2,map2):
    #h1, h2 - количество строк
    #w1, w2 - количество столбцов
    map1 = map1.split()
    map2 = map2.split()
    splittedMap = []
    crossingMaps = []
    positions = []
    counters = []
    strokes = []
    
    if(h1 <= 0 or h2 <= 0 or w1 <= 0 or w2 <= 0):
        return False
    
    if(h2 > h1 or w2 > w1):
        return False
    else:
        for x in range(len(map1)):
            pointer = 0
            sliceMap = []
            for y in range(len(map1[x])):
                mapSlice = map1[x][pointer:pointer+w2]
                if(len(mapSlice) == w2):
                    sliceMap.append(mapSlice)
                pointer += 1
            splittedMap.append(sliceMap)
        
        for x in range(len(splittedMap)):
            for y in range(len(splittedMap[x])):
                for m in range(len(map2)):
                    cross = []
                    if(splittedMap[x][y] == map2[m]):
                        cross.append(map2[m])
                        cross.append(y)
                        cross.append(x)
                        crossingMaps.append(cross)
        
        for x in range(len(crossingMaps)):
            if(map2[0] in crossingMaps[x]):
                positions.append(crossingMaps[x][1])
                strokes.append(crossingMaps[x][2])
        
        for x in range(len(positions)):
            counter = 0
            for y in range(len(crossingMaps)):
                if(crossingMaps[y][1] == positions[x] and
                    crossingMaps[y][2] >= strokes[x]):
                    counter += 1
            counters.append(counter)
            
        if(h2 in counters):
            return True
        else:
            return False
