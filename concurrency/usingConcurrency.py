from random import randint
from concurrency import sumWIthDividingIntoProcesses


elementsForSum = []
for i in range(1000000):
    elem = randint(1,1000)
    elementsForSum.append(elem)

sumWIthDividingIntoProcesses(elementsForSum, 10)
