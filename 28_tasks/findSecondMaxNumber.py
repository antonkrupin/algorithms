def findSecondMaxNumber(numbers):
    numbers.sort()
    if numbers != []:
        max1 = numbers[-1]
        max2 = numbers[0]
        
        if len(numbers) != 1:
            if numbers[0] < max1:
                max2 = numbers[0]
            numbers.pop(0)
            print(max1,max2)
            return findSecondMaxNumber(numbers)

print(findSecondMaxNumber([4,6,9,2,1,2,15,2,3,]))
