def set_bit(A,k):
    return A | (1 << k)

def clear_bit(A,k):
    return A & ~(1 << k)