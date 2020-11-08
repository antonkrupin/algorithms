"""
def findSecondMaxNumber(numbers):
    if len(numbers) > 2:
        if numbers[0] > numbers[1]:
            max1 = 0
            max2 = 1
        else:
            max1 = 1
            max2 = 0
    for i in range(2,len(numbers)):
        if numbers[i] > numbers[max1]:
            test = max1
            max1 = i
            if numbers[test] > numbers[max2]:
                max2 = test
        else:
            if numbers[i] > numbers[max2]:
                max2 = i

    print(numbers[max1])
    print(numbers[max2])
    
    if len(numbers) <= 1:
        return numbers[0]
    else:
        m = findSecondMaxNumber(numbers[1:])
        return m if m > numbers[0] else numbers[0]
    """
def findSecondMaxNumber(numbers):
    if numbers != []:
        max1 = 0
        max2 = 0
        if max1 < numbers[0]:
            max1 = numbers[0]
        if max2 < numbers[1]:
            max2 = numbers[1]
        if max1 < max2:
            max1,max2 = max2, max1
        
        numbers.pop(0)
        
        print(max1,max2)
        return findSecondMaxNumber(numbers)
    

print(findSecondMaxNumber([9,12,12,8]))