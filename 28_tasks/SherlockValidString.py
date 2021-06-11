def SherlockValidString(string):
    letters = {}
    counter = 0
    for x in range(len(string)):
        letter = string[x]
        counter += 1
        for y in range(len(string)):
            if(x != y):
                if(letter == string[y]):
                    counter += 1
        letters[letter] = counter
        counter = 0
    
    if(len(letters) == 1):
        return True
    else:
        values = list(letters.values())
        maxValue = max(letters.values())
        minValue = min(letters.values())
        if(maxValue == minValue):
            return True
        else:
            if(abs(maxValue - minValue) == 1):
                if(values.count(maxValue) == 1 or values.count(minValue) == 1):
                    return True
                else:
                    return False
            else:
                return False
