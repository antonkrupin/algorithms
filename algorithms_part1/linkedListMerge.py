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

s_list = LinkedList()
s_list1 = LinkedList()

#test = [1,2,3,4,5,0]
#test1 = [2,3,4,5,6,11]
#for i in test:
    #s_list.add_in_tail(Node(i))

#for i in test1:
    #s_list1.add_in_tail(Node(i))

print(mergeLists(s_list, s_list1))




