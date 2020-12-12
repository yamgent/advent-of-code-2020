import sys

def main():
    lines = [x.strip() for x in sys.stdin]
    pos = 0 + 0j
    wp = 10 + 1j

    for l in lines:
        char = l[0]
        val = int(l[1:])
        if char == 'N':
            wp += val * 1j
        elif char == 'S':
            wp -= val * 1j
        elif char == 'E':
            wp += val
        elif char == 'W':
            wp -= val
        elif char == 'L':
            deg = int(val / 90)
            wp *= pow(1j, deg)
        elif char == 'R':
            deg = int(val / 90)
            wp *= pow(-1j, deg)
        elif char == 'F':
            pos += wp * val

    print(str(abs(int(pos.real)) + abs(int(pos.imag))))

main()
