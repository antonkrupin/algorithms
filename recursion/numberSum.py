def numberSum(number):
    if number < 10:
        return number
    else:
        return number % 10 + numberSum(number // 10)


