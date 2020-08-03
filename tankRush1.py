def TankRush(h1,w1,map1,h2,w2,map2):
    #h1, h2 - количество строк
    #w1, w2 - количество столбцов
    map1 = map1.split()
    map2 = map2.split()
    splittedMap = []
    pointer = 0
    crossingMaps = []
    numbers = []
    
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
    
    for x in range(len(map2)):
        for y in range(len(crossingMaps)):
            test = []
            if(map2[x] == crossingMaps[y][0]):
                test.append(map2[x])
                test.append(crossingMaps[y][1])
                numbers.append(test)
                
    print(numbers)
    print(crossingMaps)
         
print(TankRush(3,4,'1234 2345 0987',2,2,'34 23 98'))
