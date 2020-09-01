def TransformTransform(numbers, n):
    transformNumbers = []
    transformNumbers1 = []

    for i in range(len(numbers)):
        for j in range(0,len(numbers)-i):
            k = i + j
            if(len(numbers[j:k+1]) != 0):
                maxNumber = max(numbers[j:k+1])
                transformNumbers.append(maxNumber)
    
    for i in range(len(transformNumbers)):
        for j in range(0,len(transformNumbers)-i):
            k = i + j
            if(len(transformNumbers[j:k+1]) != 0):
                maxNumber = max(transformNumbers[j:k+1])
                transformNumbers1.append(maxNumber)

    if(sum(transformNumbers1) % 2 == 0):
        return True
    else:
        return False
