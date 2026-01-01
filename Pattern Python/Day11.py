#Alphabet Patterns(Left Triangle Alphabet)

rows = 6
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
