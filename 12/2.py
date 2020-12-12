import sys

def add(pos, delta, count):
    return [pos[0] + (delta[0] * count), pos[1] + (delta[1] * count)]

def rot(wp, deg):
    if deg > 0:
        while deg > 0:
            deg -= 1
            wp = [wp[1], -wp[0]]
    elif deg < 0:
        while deg < 0:
            deg += 1
            wp = [-wp[1], wp[0]]

    return wp

def man(pos):
    return abs(pos[0]) + abs(pos[1])

def main():
    lines = [x.strip() for x in sys.stdin]
    pos = [0, 0]
    wp = [10, 1]

    for l in lines:
        char = l[0]
        val = int(l[1:])
        if char == 'N':
            wp = add(wp, [0, 1], val)
        elif char == 'S':
            wp = add(wp, [0, -1], val)
        elif char == 'E':
            wp = add(wp, [1, 0], val)
        elif char == 'W':
            wp = add(wp, [-1, 0], val)
        elif char == 'L':
            deg = int((-val) / 90)
            wp = rot(wp, deg)
        elif char == 'R':
            deg = int(val / 90)
            wp = rot(wp, deg)
        elif char == 'F':
            pos = add(pos, wp, val)

    print(str(man(pos)))


main()
