from linkedList import LinkedList, Node


def mergeLists(list1, list2):
    sumOfElementsList = []
    if list1.len() == list2.len():
        while list1.head is not None:
            sumOfElements = list1.head.value + list2.head.value 
            sumOfElementsList.append(sumOfElements)
            list1.head = list1.head.next
            list2.head = list2.head.next

        return [sumOfElementsList, 1]
    else:
        return [sumOfElementsList ,-1]





