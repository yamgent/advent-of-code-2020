import sys

def get_neighbours_and_self(pos):
    x, y, z, w = pos
    return {(x + dx, y + dy, z + dz, w + dw) for dx in range(-1, 2) for dy in range(-1, 2) for dz in range(-1, 2) for dw in range(-1, 2)}


def count_neighbours(pos, state):
    return sum([1 if coord != pos and coord in state else 0 for coord in get_neighbours_and_self(pos)])


def cycle(state):
    visited = set()
    new_state = set()
    for current in state:
        for coord in get_neighbours_and_self(current):
            if coord in visited:
                continue
            visited.add(coord)
            is_active = coord in state
            neighbours = count_neighbours(coord, state)
            if (is_active and 2 <= neighbours <= 3) or (not is_active and neighbours == 3):
                new_state.add(coord)

    return new_state


def main():
    state = set()
    init = [list(x) for x in sys.stdin]

    for y in range(len(init)):
        for x in range(len(init[0])):
            if init[y][x] == '#':
                state.add((x, y, 0, 0))

    for i in range(6):
        state = cycle(state)

    print(len(state))


main()
