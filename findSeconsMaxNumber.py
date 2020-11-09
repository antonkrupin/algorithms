def findSecondMaxNumber(numbers):
    numbers.sort()
    if len(numbers) >= 2:
        max1 = numbers[-1]
        max2 = numbers[0]
        
        if len(numbers) != 1:
            if numbers[0] < max1:
                max2 = numbers[0]
            numbers.pop(0)
            return findSecondMaxNumber(numbers)
        
        

print(findSecondMaxNumber([4,9,2,5,10,1]))
