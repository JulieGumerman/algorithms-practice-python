import math

def binary(arr, value):
    index = math.floor(len(arr) / 2)

    print("index number", index)
    print("value", value)

    #no length
    if len(arr) == 0:
        return False
    #one thing in array


    if arr[index] == value:
        return True
    elif value > arr[index]:
        print("should be second half of array", arr[index:])
        return binary(arr[index : ], value)
    elif value < arr[index]:
        print("should be first half of array", arr[:index])
        return binary(arr[:index], value)

print (binary([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 4))