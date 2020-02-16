def countUp(num):
    count = 1
    while count <= num:
        print(f" Number: {count}")
        count += 1
    while count >= 2:
        count -= 1
        print(f"Number: {count}")

    print("And Done!!!")

countUp(7)