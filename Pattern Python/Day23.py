#Even Number Pyramid

rows = 5
num = 2
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num += 2
    print()
