def bottles(num):
    print(f"{num} bottles of beer on the wall. {num} bottles of beer. Take one down, pass it around, {num -1} bottles of beer on the wall")
    if num <= 1:
        print("The party's over, and this place is a mess")
        return
    else: 
        bottles(num-1)

bottles(99)