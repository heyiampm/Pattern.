#Hollow diamond star pattern
row = 5

# top half (including middle)
for i in range(1, row + 1):
    # print leading spaces
    print(" " * (row - i), end="")

    # print the pattern stars / spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# bottom half
for i in range(row - 1, 0, -1):
    # print leading spaces
    print(" " * (row - i), end="")

    # print stars / spaces
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

