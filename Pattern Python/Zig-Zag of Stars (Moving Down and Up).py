n = 5
indent = 0
step = 1

for _ in range(2 * n - 2):
    print(" " * indent + "*")
    if indent == n - 1:
        step = -1
    elif indent == 0:
        step = 1
    indent += step
