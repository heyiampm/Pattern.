#Butter fly Pattern.

n = int(input("Enter number of rows: "))

# Upper half wings
for i in range(1, n + 1):
    # left stars
    for j in range(i):
        print("*", end="")
    # inner spaces
    for k in range(2 * (n - i)):
        print(" ", end="")
    # right stars
    for j in range(i):
        print("*", end="")
    print()

# Lower half wings
for i in range(n, 0, -1):
    # left stars
    for j in range(i):
        print("*", end="")
    # inner spaces
    for k in range(2 * (n - i)):
        print(" ", end="")
    # right stars
    for j in range(i):
        print("*", end="")
    print()
