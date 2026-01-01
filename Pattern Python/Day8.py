#Pascal’s Triangle

def print_pascals_triangle(rows):
    for i in range(rows):
        val = 1
        for j in range(i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)
        print()

print_pascals_triangle(5)