#Dimond Star pattern

n = 5
# upper
for i in range(n):
    print(" "*(n-i-1) + "* "*(i+1))
# lower
for i in range(n-1):
    print(" "*(i+1) + "* "*(n-1-i))
