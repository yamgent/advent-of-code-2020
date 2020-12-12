import sys

DELTA = [[1, 0], [0, -1], [-1, 0], [0, 1]]

def add(pos, delta, mag):
    return [pos[0] + (delta[0] * mag), pos[1] + (delta[1] * mag)]

def rot(direction, deg):
    direction += deg
    while direction < 0:
        direction += len(DELTA)
    while direction >= len(DELTA):
        direction -= len(DELTA)
    return direction

def main():
    lines = [x.strip() for x in sys.stdin]
    pos = [0, 0]
    direction = 0

    for l in lines:
        char = l[0]
        val = int(l[1:])
        if char == 'N':
            pos = add(pos, DELTA[3], val)
        elif char == 'S':
            pos = add(pos, DELTA[1], val)
        elif char == 'E':
            pos = add(pos, DELTA[0], val)
        elif char == 'W':
            pos = add(pos, DELTA[2], val)
        elif char == 'L':
            deg = int((-val) / 90)
            direction = rot(direction, deg)
        elif char == 'R':
            deg = int(val / 90)
            direction = rot(direction, deg)
        elif char == 'F':
            pos = add(pos, DELTA[direction], val)

    print(str(abs(pos[0]) + abs(pos[1])))


main()
