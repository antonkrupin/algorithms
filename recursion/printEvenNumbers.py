def printEvenNumbers(numbers):
    if numbers != []:
        if numbers[0] % 2 == 0:
            print(numbers.pop(0))
            return printEvenNumbers(numbers)
        else:
            numbers.pop(0)
            return printEvenNumbers(numbers)


