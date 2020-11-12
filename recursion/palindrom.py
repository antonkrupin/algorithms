def palindrom(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrom(string[1:-1])
        else:
            return False
