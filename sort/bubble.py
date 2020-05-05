def bubbleSort(array, controlArray):
    if len(controlArray) == 0:
        return array
    
    for i in array:
        if i > next(i):
            array[i], array[next(i)] = array[next(i)], array[i]
    
    return bubbleSort(array, controlArray[:-1])


arrayToUse = [5, 1, 2, 4, 3]
print(bubbleSort(arrayToUse, arrayToUse))