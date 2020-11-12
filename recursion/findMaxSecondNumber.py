def findSecondMaxNumber(numbers):
    if len(numbers) >= 2:
        numbers.sort()
        if numbers[0] > numbers[1]:
            max1 = numbers[0]
            max2 = numbers[1]
        else:
            max1 = numbers[1]
            max2 = numbers[0]

        numbers.pop(0)
        numbers.pop(0)
        
        def recursion(max1, max2):
            if numbers != []:
                if numbers[0] > max1:
                    test = max1
                    max1 = numbers[0]
                    if test > max2:
                        max2 = test
                else:
                    if numbers[0] > max2 and numbers[0] > max1:
                        max2 = numbers[0]
                    
                numbers.pop(0)
                return recursion(max1, max2)
            else:
                return [max1,max2]

        return recursion(max1, max2)
    else:
        return numbers[0]

print(findSecondMaxNumber([23,12,23,17]))
