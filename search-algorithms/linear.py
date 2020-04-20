def linearSearch(arr, val):
    for i in arr:
        if i == val:
            return arr.index(i)
    return -1

print(linearSearch(["a", "b", "c", "d", "e"], "b"))