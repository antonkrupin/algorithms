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
    testing = []
    testing1 = []
    if(h1 <= 0 or h2 <= 0 or w1 <= 0 or w2 <= 0):
        return False
    
    if(h2 > h1 or w2 > w1):
        return False
    else:
        for x in range(len(map1)):
            pointer = 0
            for y in range(len(map1[x])):
                if(len(map1[x][pointer:pointer+w2]) == w2):
                    test = map1[x][pointer:pointer+w2]
                    testing = []
                    if(test == map2[0]):
                        testing.append(1)
                        for z in range(x+1,len(map1)):
                            r = map1[z][pointer:pointer+w2]
                            for i in range(1,len(map2)):
                                if(r == map2[i]):
                                    testing.append(1)
                                else:
                                    testing.append(0)
                                    
                    if(len(testing) != 0):
                        testing1.append(testing)
                pointer += 1
        print(testing1)
