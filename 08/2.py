import sys

class State:
    def __init__(self, visited, acc, pc):
        self.visited = visited
        self.acc = acc
        self.pc = pc


def main():
    lines = [[x[0], int(x[1])] for x in [x.strip().split(' ') for x in sys.stdin]]
    saved = None
    state = State(set(), 0, 0)

    while True:
        if state.pc >= len(lines):
            print(state.acc)
            return
        elif state.pc in state.visited:
            # restore no-replace version
            state = saved
            saved = None
        else:
            state.visited.add(state.pc)

            inst, val = lines[state.pc]
            if inst == 'nop':
                if saved:
                    # normal nop
                    state.pc += 1
                else:
                    # save no-replace version
                    saved = State(set(state.visited), state.acc, state.pc + 1)

                    # do jmp
                    state.pc += val
            elif inst == 'acc':
                state.acc += val
                state.pc += 1
            elif inst == 'jmp':
                if saved:
                    # normal jmp
                    state.pc += val
                else:
                    # save no-replace version
                    saved = State(set(state.visited), state.acc, state.pc + val)

                    # do nop
                    state.pc += 1


main()
