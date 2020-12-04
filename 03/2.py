import sys

def count(lines, dx, dy):
    tree = 0

    w = len(lines[0])
    h = len(lines)
    x = 0
    for y in range(dy, h, dy):
        x += dx
        if x >= w:
            x -= w
        if lines[y][x] == '#':
            tree += 1

    return tree


def main():
    lines = [l.strip() for l in sys.stdin]
    a = count(lines, 1, 1)
    b = count(lines, 3, 1)
    c = count(lines, 5, 1)
    d = count(lines, 7, 1)
    e = count(lines, 1, 2)
    # print(a, b, c, d, e)
    print(str(a * b * c * d * e))

main()
