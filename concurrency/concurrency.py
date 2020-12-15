import time
from random import randint
from threading import Thread

elementsForSum = []
for i in range(10):
    elem = randint(1,10)
    elementsForSum.append(elem)


def sum_numbers_full(elements, processQuantity):
    results = {}
    funcitons = []

    for i in range(processQuantity):
        funcitons.append(i)
    
    checker = 0
    value = len(elements)//processQuantity
    for i in funcitons:
        name = 'f' + str(i)
        print(elements[checker:checker+value])
        name = Thread(target=test_func, name="Threa", args=(i,elements[checker:checker+value], results))
        checker += value
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

test = sum_numbers_full(elementsForSum, 6)
sum1 = 0
for i in elementsForSum:
    sum1 += i

print(test)
print(sum1)
