def Keymaker(k):
    doors = []
    for x in range(0,k+1):
        doors.append(0)
        
    for x in range(1,len(doors)):
        if x == 1:
            for j in range(1,len(doors)):
                doors[j] = 1
        else:
            for j in range(1,len(doors)):
                if j%x == 0:
                    if doors[j] == 0:
                        doors[j] = 1
                    else:
                        doors[j] = 0
        
    string = ''.join(map(str,doors[1:]))
    return string
