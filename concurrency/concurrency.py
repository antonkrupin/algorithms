import time
from random import randint
from threading import Thread


def sumWIthDividingIntoProcesses(elements, processorsQuantity):
    if processorsQuantity > 0:
        results = {}
        functions = []
        dividedElements = []
        resultSum = 0

        for i in range(processorsQuantity):
            dividedElements.append([])
            functions.append(i)

        for i in range(len(elements)):
            index = i % processorsQuantity
            dividedElements[index].append(elements[i])

        for i in functions:
            name = 'f' + str(i)
            name = Thread(target=sumElements, name=f'Thread {str(i)}', args=(i,dividedElements[i], results))
            name.start()      

        for key in results:
            resultSum += results[key]

        return [resultSum, 1]
    else:
        return [0, -1]
    
def sumElements(id, elements, results):
    sum = 0
    for i in elements:
        sum += i
    results[id] = sum

