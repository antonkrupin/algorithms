def odometer(oksana = []):
    distance = 0
    hours = []
    speed = []
    i = 0
    while(i < len(oksana)):
        if(i == 1):
            hours.append(oksana[i])
        else:
            if(i%2 != 0):
                hours.append(oksana[i] - oksana[i-2])
        i = i + 1
        
    i = 0
    while(i < len(oksana)):
        if(i%2 == 0):
            speed.append(oksana[i])
        i = i + 1
        
    i = 0
    while(i < len(hours)):
        distance = distance + (speed[i] * hours[i])
        i = i + 1
        
    return distance