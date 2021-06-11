def Football(numbers, n):
    sortedNumbers = list(numbers)
    sortedNumbers.sort()
    if(numbers == sortedNumbers):
        return False
        
    def flatten(lst):
        while lst:
            sublist = lst.pop(0)
            if isinstance(sublist, list):
                lst = sublist + lst
            else:
                yield sublist
    
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            numbersCopy = list(numbers)
            if(i != j):
                number1 = numbersCopy[i]
                number2 = numbersCopy[j]
                numbersCopy[i] = number2
                numbersCopy[j] = number1
            if(numbersCopy == sortedNumbers):
                return True
    
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            numbersCopy = list(numbers)
            length = len(numbers)-j
            numbersSlice1 = numbersCopy[0:i]
            numbersSlice = numbersCopy[i:length]
            reversedNumbersSlice = numbersSlice[::-1]
            if(length <= 5):
                if(len(numbersCopy[length:]) != 0):
                    reversedNumbersSlice.append(numbersCopy[length:])
                if(len(numbersSlice1) != 0):
                    reversedNumbersSlice.insert(0,numbersSlice1)
            
            if(list(flatten(reversedNumbersSlice)) == sortedNumbers):
                return True
            
    return False
