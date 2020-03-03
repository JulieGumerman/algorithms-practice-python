def sheep_count(sheep):
    print(f"{sheep} sheep jumping over the fence")
    if sheep < 1:
        print('sound asleep')
    else:
        sheep_count(sheep-1)

sheep_count(50)

def twister(a, b):
    print(f"How much {a} would a {a + b} {b} if a {a + b} could {b} {a}")

twister("wood", "chuck")