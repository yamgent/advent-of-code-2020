import sys

def main():
    lines = [l.strip() for l in sys.stdin]
    tree = 0

    w = len(lines[0])
    h = len(lines)
    x = 0
    for y in range(1, h):
        x += 3
        if x >= w:
            x -= w
        if lines[y][x] == '#':
            tree += 1

    print(tree)


main()
