def two_sort(array):
    array2 = array.copy()
    array2.sort(key=None, reverse=False)
    s = ""
    for x in array2[0]:
        s += x + "***"
    return s[0:-3]
