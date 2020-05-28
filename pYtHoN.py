def pYtHoN(PyThOn):
    n = 2
    for i in range(3):
        n = n*n
    n = n*(2**PyThOn)
    return n
print (pYtHoN(0)/pYtHoN(-3))