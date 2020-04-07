import math

def repeatedString(s, n):
    remainder = n % len(s)
    print("REMAINDER", remainder)
    divided = math.floor(n / len(s))
    infiniteArray = list(s)
    print(infiniteArray)
    little_bit = infiniteArray[0:remainder]
    big_chunk = infiniteArray * divided
    finiteArray = big_chunk + little_bit
    print(finiteArray)

    counter = 0

    for i in finiteArray:
        if i == 'a':
            counter += 1

    return print(counter)

repeatedString("aba", 10)