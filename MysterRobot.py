def MisterRobot(n, data):
    if(data != sorted(data)):
        def checkArray(data):
            x=0
            for x in range(len(data)):
                if(x+3 <= len(data)):
                    dataSlice = data[x:x+3]
                    a = dataSlice[0]
                    b = dataSlice[1]
                    c = dataSlice[2]
                    if(a < b and b < c):
                        continue
                    else:
                        a = dataSlice[1]
                        b = dataSlice[2]
                        c = dataSlice[0]
                        
                        if(a < b and b < c):
                            dataSlice[0] = a
                            dataSlice[1] = b
                            dataSlice[2] = c
                            data[x:x+3] = dataSlice
                            if(data == sorted(data)):
                                return True
                        else:
                            a = dataSlice[2]
                            b = dataSlice[0]
                            c = dataSlice[1]
                        
                            dataSlice[0] = a
                            dataSlice[1] = b
                            dataSlice[2] = c
                        
                            data[x:x+3] = dataSlice
                            if(data == sorted(data)):
                                return True
                else:
                    return data
                    
        for x in range(n):
            if(checkArray(data) == True):
                return True
            else:
                test = checkArray(data)
                if(test == True):
                    return True
                else:
                    checkArray(test)
                
        if(data != sorted(data)):
            return False
    else:
        return False
    
print(MisterRobot(8,[3,4,5,1,2,6,7,8]))
