def ConquestCampaign(n, m, battalion):
    height = n
    width = m
    #массив для координат поля
    battleFeield = []
    #массив для координат по высоте
    attackPointsHeight = []
    #массив для координат по ширине
    attackPointsWidth = []
    
    #проверка на дублирование координат
    attackPoints = []
    for i in battalion: 
        if i not in attackPoints: 
            attackPoints.append(i)
    
    #разбиение координат точек нападения
    for x in range(len(attackPoints)):
        if(attackPoints[x][0] <= height and attackPoints[x][1] <= width):
            attackPointsHeight.append(attackPoints[x][0]-1)
            attackPointsWidth.append(attackPoints[x][1]-1)
    
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
    
    #выставление координат точек нападения
    for x in range(len(attackPointsHeight)):
        battleFeield[attackPointsHeight[x]][attackPointsWidth[x]] = 1
    
    days = 0
    
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
                if(battleFeield[i][j] == 0 and i < counterH-1):
                    if(battleFeield[i+1][j] == 1):
                        battleFeield[i][j] = 0.5
            
                if(battleFeield[i][j] == 0.5):
                    battleFeield[i][j] = 1
            
                if(battleFeield[i][j] == 0 and j < counterW-1):
                    if(battleFeield[i][j+1] == 1):
                        battleFeield[i][j] = 0.5
        
                if(i != 0 and battleFeield[i][j] == 0):
                    if(battleFeield[i-1][j] == 1):
                        battleFeield[i][j] = 0.5
        
                if(j != 0 and battleFeield[i][j] == 0):
                        if(battleFeield[i][j-1] == 1):
                            battleFeield[i][j] = 0.5
        days = days + 1
    return days
