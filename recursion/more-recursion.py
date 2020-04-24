#recursion counts number of items in list

#maximum number in list
def max_number(arr, largest):
    if arr[0] > largest: 
        arr[0] = largest
    #base case: nothing left in array
    if arr == []:
        return largest
    #recursive case:
    else:
        max_number(arr[1:], largest)

print(max_number([3,1,4,2], 0))
#binary search; base case and recursive case
