from collections import deque

def parse_input():
    p1, p2 = deque(), deque()

    # line is 'Player 1'
    input()

    line = input()
    while line:
        p1.append(int(line))
        line = input()

    # line is 'Player 2'
    input()

    try:
        while True:
            p2.append(int(input()))
    except EOFError:
        pass

    return p1, p2


def calc_score(pall):
    return sum([(i + 1) * v for i, v in enumerate(reversed(pall))])


def play(op1, op2):
    p1 = deque(op1)
    p2 = deque(op2)
    previous_states = { (tuple(p1), tuple(p2)) }
    # print(p1, p2)

    while len(p1) > 0 and len(p2) > 0:
        p1_cur = p1.popleft()
        p2_cur = p2.popleft()

        if (tuple(p1), tuple(p2)) in previous_states:
             return True, None
        previous_states.add((tuple(p1), tuple(p2)))

        p1_roundwin = p1_cur == max(p1_cur, p2_cur)
        if p1_cur <= len(p1) and p2_cur <= len(p2):
            p1_roundwin, ignore = play(list(p1)[:p1_cur], list(p2)[:p2_cur])

        pwin = p1 if p1_roundwin else p2
        pwin.append(p1_cur if p1_roundwin else p2_cur)
        pwin.append(p2_cur if p1_roundwin else p1_cur)

    p1_win = len(p1) > 0
    pall = p1 if len(p1) > 0 else p2
    return p1_win, pall


def main():
    p1, p2 = parse_input()
    p1_win, pall = play(p1, p2)
    # print('Player 1 won?', p1_win)
    print(calc_score(pall))


main()
