#Hourglass Star Pattern

n = 5

# Upper
for i in range(n-1):
    print(" " * i + "* " * (2*(n-i)-1))
# Lower
for i in range(n):
    print(" " * (n-i-1) + "* " * (2*i+1))
