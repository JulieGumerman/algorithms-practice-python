def reverseArray(arr):
    newArray = []
    for item in arr:
        newArray.insert(0, item)
    print(f"reverse array function: {newArray}")

def reverseArrayNumberTwo(arr):
    aNewArray = []
    for item in reversed(arr):
        aNewArray.append(item)
    print(f"reverse array function: {aNewArray}")


reverseArray(["yes", "I", "like", "cheese"])
reverseArrayNumberTwo(["yes", "I", "like", "cheese"])