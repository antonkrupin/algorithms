def ConquestCampaign(n,m,l,battalion=[]):
    #массив для координат начальных точек нападения
    startCoordsN = [] #координаты по X
    startCoordsM = [] #координаты по Y
    i = 0
    daysToCapture = 1
    #распределение начальных точек по массивам
    while(i < len(battalion)):
        if(i%2 == 0):
            startCoordsN.append(battalion[i]-1)
        else:
            startCoordsM.append(battalion[i]-1)
        i = i + 1
        
    #создание карты
    mapHeight = n
    mapWidth = m
    campainMap = [0] * mapHeight
    for i in range(mapHeight):
        campainMap[i] = [0] * mapWidth
        
    #добавление начальных точек
    for i in range(len(startCoordsN)):
        campainMap[startCoordsN[i]][startCoordsM[i]] = 1
    
    #вывод карты (для теста)
    for row in campainMap:
        for elem in row:
            print(elem, end=' ')
        print()
    
    for row in campainMap:
        for elem in row:
            if(elem == 1):
                print(row.index(elem), end=' ')
                print(campainMap.index(row))
            
    
print(ConquestCampaign(3,4,2,[2,2,3,4]))


def test():
    days = 1
    testArray = [0,0,1,0,0]
    while 0 in testArray:
        days = days + 1
        for i in range(len(testArray)):
            print(testArray)
            print(i)
            if(testArray[i] == 1):
                counter = testArray.index(testArray[i])
                if(counter == len(testArray)-1):
                    testArray[counter - 1] = 1
                else:
                    testArray[counter + 1] = 1
                    testArray[counter - 1] = 1
    return days 
print(test())