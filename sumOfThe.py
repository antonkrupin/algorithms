def SumOfThe(n,data):
    sumData = 0
    sliceArray = []
    sumOfElements = 0
    
    for x in range(n):
        element = data[x]
        sumData = 0
        if(x == 0):
            sliceArray = data[1:]
            for i in range(len(sliceArray)):
                sumData = sumData + sliceArray[i]
            
            if (element == sumData):
                sumOfElements = element
        if(x == n-1):
            sliceArray = data[:-1]
            for i in range(len(sliceArray)):
                sumData = sumData + sliceArray[i]
            
            if (element == sumData):
                sumOfElements = element
            
        if(x != 0 and x != n-1):
            sliceArray = data[:x] + data[x+1:]
            for i in range(len(sliceArray)):
                sumData = sumData + sliceArray[i]
            
            if (element == sumData):
                sumOfElements = element
    
    return sumOfElements