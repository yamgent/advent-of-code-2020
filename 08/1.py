import sys


def main():
    lines = [[x[0], int(x[1])] for x in [x.strip().split(' ') for x in sys.stdin]]
    visited = set()
    acc = 0
    pc = 0

    while True:
        if pc in visited:
            print(acc)
            return

        visited.add(pc)
        inst, val = lines[pc]
        if inst == 'nop':
            pc += 1
        elif inst == 'acc':
            acc += val
            pc += 1
        elif inst == 'jmp':
            pc += val


main()
