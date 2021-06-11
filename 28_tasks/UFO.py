def UFO(n,data,octal):
    dectyptedData = []
    stringCryptedData = []
    
    for x in range(len(data)):
        stringCryptedData.append(str(data[x]))
    
    def decryption(data,octal,dectyptedData):
        if(octal):
            basis = 8
        else:
            basis = 16
            
        for x in range(len(data)):
            m = data[x]
            powNumber = len(m)-1
            dectyptedSlice = 0
            for i in range(len(m)):
                dectyptedSlice += int(m[i])*basis**powNumber
                powNumber -= 1
            dectyptedData.append(dectyptedSlice)
        return dectyptedData
        
    return decryption(stringCryptedData,octal,[])
