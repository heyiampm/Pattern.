def zigzag_wave(n):
    rows = n
    cols = 4 * n  # wider so zig‑zag can move left and right

    for i in range(rows):
        for j in range(cols):
            # star moves diagonally down then up
            if (j % (2 * rows)) == i or (j % (2 * rows)) == (2 * rows - i - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example: zigzag wave with 5 rows
zigzag_wave(5)
