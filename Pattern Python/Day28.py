# Top heart

n = 5

for i in range(n//2, n, 2):
    for j in range(1, n-i, 2):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(1, n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

# Bottom heart
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end=" ")
    for j in range(1, i*2):
        print("*", end=" ")
    print()
