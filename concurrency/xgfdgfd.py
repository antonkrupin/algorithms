import time
from random import randint
from threading import Thread

elementsForSum = []
for i in range(10000000):
    elem = randint(1,1000)
    elementsForSum.append(elem)


def sum_numbers_full(elements, processorsQuantity):
    results = {}
    funcitons = []
    elemChunc = []
    elementsInChunc = len(elements)//processorsQuantity

    for i in range(0, len(elements), elementsInChunc+1):
        elemChunc.append(elements[i:i + elementsInChunc+1])

    for i in range(processorsQuantity):
        funcitons.append(i)

    while len(elemChunc) <= len(funcitons):
        elemChunc.append([])
    
    for i in funcitons:
        name = 'f' + str(i)
        name = Thread(target=test_func, name="Threa", args=(i,elemChunc[i], results))
        name.start()
    finalSum = 0
    for key in results:
        finalSum += results[key]
    
    return finalSum
    
def test_func(id, elements, results):
    sum = 0
    for i in elements:
        sum += i
    results[id] = sum

test = sum_numbers_full(elementsForSum, 1)
sum1 = 0
for i in elementsForSum:
    sum1 += i

print(test)
print(sum1)
