def SynchronizingTables(n,ids,salary):
    nonSortedIds = []
    for x in range(len(ids)):
        nonSortedIds.append(ids[x])
    
    sortedIds = []
    sortedSalary = []
    rightSalary = []
    dict = {}
    
    def bubble(array):
        N = len(array)
        for i in range(N-1):
            for j in range(N-i-1):
                if array[j] > array[j+1]:
                    buff = array[j]
                    array[j] = array[j+1]
                    array[j+1] = buff
        return array
    
    sortedIds = bubble(ids)
    sortedSalary = bubble(salary)
    
    for x in range(len(sortedIds)):
        dict[sortedIds[x]] = sortedSalary[x]
    
    for x in range(len(nonSortedIds)):
        rightSalary.append(dict[nonSortedIds[x]])
        
    return rightSalary
