def list_length(elementsList):
    if elementsList == []:
        return 0
    else:
        elementsList.pop(0)
        return 1 + list_length(elementsList)


