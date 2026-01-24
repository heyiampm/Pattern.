n = 5

# number of columns (wide enough for a zigzag pattern)
cols = 2 * n

for i in range(1, n + 1):
    for j in range(1, cols + 1):
        # print star in zigzag positions
        if (i + j) % 4 == 0 or (i == 2 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()  # newline after each row
