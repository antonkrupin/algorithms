def UFO(n,data,octal):
    dectyptedData = []
    if(octal):
        for x in range(len(data)):
            decrypted = int(str(data[x]),8)
            dectyptedData.append(decrypted)
    else:
        for x in range(len(data)):
            decrypted = int(str(data[x]),16)
            dectyptedData.append(decrypted)
    return dectyptedData