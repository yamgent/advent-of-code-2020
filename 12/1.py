import sys

def main():
    lines = [x.strip() for x in sys.stdin]
    pos = 0 + 0j
    direction = 1 + 0j

    for l in lines:
        char = l[0]
        val = int(l[1:])
        if char == 'N':
            pos += val * 1j
        elif char == 'S':
            pos -= val * 1j
        elif char == 'E':
            pos += val
        elif char == 'W':
            pos -= val
        elif char == 'L':
            deg = int(val / 90)
            direction *= pow(1j, deg)
        elif char == 'R':
            deg = int(val / 90)
            direction *= pow(-1j, deg)
        elif char == 'F':
            pos += direction * val

    print(str(abs(int(pos.real)) + abs(int(pos.imag))))

main()
