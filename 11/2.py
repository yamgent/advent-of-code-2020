import sys

DIR = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ]

def out_of_range(grid, y, x):
    return y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0])


def scan_occupied(grid, y, x, dy, dx):
    y += dy
    x += dx
    while not out_of_range(grid, y, x):
        if grid[y][x] == '#':
            return True
        elif grid[y][x] == 'L':
            return False

        y += dy
        x += dx

    return False


def update(old):
    new = []
    changed = False

    for y in range(0, len(old)):
        new_row = old[y][:]

        for x in range(0, len(old[0])):
            pos_char = old[y][x]
            if pos_char == '.':
                continue
            total_occ = sum([1 if scan_occupied(old, y, x, d[0], d[1]) else 0 for d in DIR])
            if pos_char == 'L' and total_occ == 0:
                new_row[x] = '#'
                changed = True
            elif pos_char == '#' and total_occ >= 5:
                new_row[x] = 'L'
                changed = True

        new.append(new_row)
    return new, changed


def count_occupied(grid):
    return sum([sum([1 if l == '#' else 0 for l in row]) for row in grid])


def print_grid(grid):
    print('\n'.join([''.join(row) for row in grid]))


def main():
    grid = [list(x.strip()) for x in sys.stdin]
    new_grid, changed = grid, True

    while changed:
        new_grid, changed = update(new_grid)

    print(count_occupied(new_grid))


main()
