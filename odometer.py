def odometer(oksana = []):
    distance = 0
    i = 0
    while(i < len(oksana)):
        if (i % 2) == 0:
            distance = distance + oksana[i]
        i = i + 1
    return distance