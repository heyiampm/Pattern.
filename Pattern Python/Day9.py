# Floyd’s Triangle (Sequential numbers)

rows = 5
num = 1
for i in range(rows):
    for j in range(i + 1):
        print(num, end=" ")
        num += 1
    print()
