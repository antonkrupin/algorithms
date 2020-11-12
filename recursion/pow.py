def numberPow(n,m):
    if m == 1:
        return n
    else:
        return n * numberPow(n,m-1)
