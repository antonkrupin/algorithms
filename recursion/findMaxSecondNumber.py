def findSecondMaxNumber(numbers):
    if len(numbers) >= 2:
        numbers.sort()
        
        max1 = numbers[0]
        max2 = numbers[0]
                
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

print(findSecondMaxNumber([15,15,15,3,7,12,13,15,15,15,11,12]))
