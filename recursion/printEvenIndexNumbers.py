def printEvenIndexNumbers(numbers):
    if numbers != []:
        if len(numbers)%2 == 0:
            print(numbers[0])
            numbers.pop(0)
            numbers.pop(0)
            return printEvenIndexNumbers(numbers)
        else:
            print(numbers[0])
            numbers.pop(0)
            if numbers != []:
                numbers.pop(0)
            return printEvenIndexNumbers(numbers)

print(printEvenIndexNumbers([2,3,4,5,6,7,8,9,0]))
