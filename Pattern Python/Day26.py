#Hollow Diamond Star Pattern

n = 5

# Top half
for i in range(1, n+1):
    print(' '*(n-i) + '*' + ' '*(2*i-3) + ('*' if i > 1 else ''))

# Bottom half
for i in range(n-1, 0, -1):
    print(' '*(n-i) + '*' + ' '*(2*i-3) + ('*' if i > 1 else ''))
