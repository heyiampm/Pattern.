#Fancy Double Diamond Star Pattern

n = 5

# Top part as diamond top
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i - 1))

# Bottom triangle
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i - 1))