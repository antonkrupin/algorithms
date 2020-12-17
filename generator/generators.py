def infinityGenetator(values):
    if len(values) > 0:
        results = {}
        maxValue = max(values)
        processLinks = []

        for i in range(len(values)):
            ID = 'ID' + str(i)
            results[ID] = None

        for key in results:
            valueIndex = int(key[2:])
            processLink = long_process(key, values[valueIndex])
            processLinks.append(processLink)
        
        for i in range(maxValue):
            for key in results:
                if results[key] is None: 
                    processLinkIndex = int(key[2:])
                    results[key] = next(processLinks[processLinkIndex])
        
        return [results, 1]
    else:
        return [results, -1]

def long_process(id,n):
    sum = 0
    if n > 0:
        for x in range(n):
            sum += x
            if x < n-1:
                yield
            else:
                yield sum
    else:
        yield sum


