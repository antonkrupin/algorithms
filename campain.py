def ConquestCampaign(n, m, l, battalion):
    
    daysToCapture = 1
    height = n
    width = m
    battleFeield = []
    attackPointsLength = l
    #массив точек атаки, в котором нет дублей
    attackPoints = []
    #координаты точек высадки по высоте
    attackCoordsN = []
    #координаты точек высадки по ширине
    attackCoordsM = []
    
    #функция разбиения массива с координатами на пары
    def group(iterable, count):
        return zip(*[iter(iterable)] * count)
    
    if (attackPointsLength != len(battalion)/2):
        return daysToCapture
        
    if (height <= 0 or width <= 0):
        return daysToCapture
        
    if (len(battalion) == 0):
        return daysToCapture
        
    coordsPairs = list(group(battalion, 2))
    
    #проверка на дублирование координат
    attackPoints = []
    for i in coordsPairs: 
        if i not in attackPoints and len(i) == 2: 
            attackPoints.append(i)
    
    print(attackPoints)
    #формирование базовой карты
    counterH = height
    
    while(counterH != 0):
        counterW = width
        battleLine = []
        while(counterW != 0):
            battleLine.append(0)
            counterW = counterW - 1
        battleFeield.append(battleLine)
        counterH = counterH - 1
        
    #расстановка точек атаки
    for x in range(len(attackPoints)):
        n = attackPoints[x][0]
        m = attackPoints[x][1]
        if((n >= 0 and m >= 0) and (n <= height and m <= width)):
            battleFeield[n-1][m-1] = 1
    
    for x in battleFeield:
        print(x)
    counterH = len(battleFeield)
    counterW = len(battleFeield[0])
    flag = True
    checkZero = 0
    
    while(flag):
        for line in range(len(battleFeield)):
            if(not 0 in battleFeield[line]):
                checkZero = checkZero + 1
            if(checkZero == counterH):
                flag = False
        
        for i in range(len(battleFeield)):
            for j in range(len(battleFeield[i])):
                if(battleFeield[i][j] == 0.5):
                    battleFeield[i][j] = 1
                    
                if(battleFeield[i][j] == 0 and i < counterH-1):
                    if(battleFeield[i+1][j] == 1):
                        battleFeield[i][j] = 0.5
            
                if(battleFeield[i][j] == 0 and j < counterW-1):
                    if(battleFeield[i][j+1] == 1):
                        battleFeield[i][j] = 0.5
        
                if(i != 0 and battleFeield[i][j] == 0):
                    if(battleFeield[i-1][j] == 1):
                        battleFeield[i][j] = 0.5
        
                if(j != 0 and battleFeield[i][j] == 0):
                        if(battleFeield[i][j-1] == 1):
                            battleFeield[i][j] = 0.5
                            
        print('---------------------------')
        for x in battleFeield:
            print(x)
        daysToCapture = daysToCapture + 1
    return daysToCapture
