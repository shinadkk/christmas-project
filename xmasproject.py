n = input("what is your name?")
width = int(input("Enter Chirstmas Tree Width   = "))
height = int(input("Enter Chirstmas Tree Height = "))

space = width * height
n = 1

print("MERRY CHRISTMAS + n")
alphabet = 65

for x in range(1, height + 1):
    for i in range(n, width + 1):
        for j in range(space, i - 1, -1):
            print(end = ' ')
        for k in range(1, i + 1):
            print('*', end = ' ')
        print()
    n = n + 2
    width = width + 2

for i in range(1, height):
    for j in range(space - 3, -1, -1):
        print(end = ' ')
    for k in range(1, height):
        print('*', end = ' ')
    print()
    print(MOHAMMED SHINAD KK)
    print(S1 CSE)