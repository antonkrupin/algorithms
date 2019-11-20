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