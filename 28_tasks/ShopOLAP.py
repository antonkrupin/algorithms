def ShopOLAP(n,saleGoods):
    splittedGoods = []
    summOfGoods = []
    for x in range(len(saleGoods)):
        splittedGoods.append(saleGoods[x].split())
    
    for x in range(len(splittedGoods)):
        splittedGoods[x][1] = int(splittedGoods[x][1])
    
    for i in range(len(splittedGoods)):
        m = splittedGoods[i]
        for j in range(len(splittedGoods)):
            if(j != i):
                if(m[0] == splittedGoods[j][0]):
                    m[1] += splittedGoods[j][1]
                    splittedGoods[j][1] = False
    
    for x in range(len(splittedGoods)):
        if(splittedGoods[x][1] != False):
            summOfGoods.append(splittedGoods[x])
    
    for x in range(len(summOfGoods)):
        a = summOfGoods[x]
        for i in range(len(summOfGoods)):
            if(i != x):
                if(a[1] > summOfGoods[i][1]):
                    b = summOfGoods[i]
                    c = summOfGoods[x]
                    summOfGoods[x] = b
                    summOfGoods[i] = c
         
    for x in range(len(summOfGoods)):
        a = summOfGoods[x]
        for i in range(len(summOfGoods)):
            if(i != x):
                if(a[1] == summOfGoods[i][1]):
                    if(a[0] < summOfGoods[i][0]):
                        b = summOfGoods[i]
                        c = summOfGoods[x]
                        summOfGoods[x] = b
                        summOfGoods[i] = c
    
    for x in range(len(summOfGoods)):
        summOfGoods[x] = summOfGoods[x][0] + ' ' + str(summOfGoods[x][1])
    
    return summOfGoods    
