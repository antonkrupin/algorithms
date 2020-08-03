def Unmanned(roadLength, n, track):
    travelTime = 1
    trafficLightsLocation = []
    
    for x in range(len(track)):
        if(track[x][0] < roadLength):
            trafficLightsLocation.append(track[x][0])
    if(len(trafficLightsLocation) != 0):
        for x in range(1,roadLength+1):
            for i in range(len(trafficLightsLocation)):
                if(x == trafficLightsLocation[i]):
                    if(travelTime < track[i][1]):
                        travelTime += track[i][1] - x
                        break
                    if(travelTime == track[i][1]):
                        travelTime += 1
                        break
                    if(travelTime > track[i][1] and travelTime < track[i][2]):
                        travelTime += 1
                        break
                    if(travelTime > track[i][1] and travelTime > track[i][2]):
                        if(travelTime%(track[i][1]+track[i][2]) <= track[i][1]
                            and (travelTime%(track[i][1]+track[i][2]) != 0)):
                            travelTime += track[i][1] - travelTime%(track[i][1]+track[i][2])
                            break
                        else:
                            travelTime += 1
                            break
                else:
                    travelTime += 1
                    break
    else:
        travelTime = roadLength
    return travelTime
