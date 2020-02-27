def add_array(arr , n):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + add_array(arr[1:], n)


arr = [1,2,3,4,5]
n = len(arr)
answer = add_array(arr, n)
print(answer)


#better answer
def sum(list):
    if list == []:
        return
    return list[0] + sum(list[1:])