from collections import deque

def main():
    # == parse input ==
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

    # == simulate ==
    while len(p1) > 0 and len(p2) > 0:
        p1_cur = p1.popleft()
        p2_cur = p2.popleft()
        pwin = p1 if p1_cur == max(p1_cur, p2_cur) else p2
        pwin.append(max(p1_cur, p2_cur))
        pwin.append(min(p1_cur, p2_cur))

    pall = p1 if len(p1) > 0 else p2
    score = sum([(i + 1) * v for i, v in enumerate(reversed(pall))])
    print(score)


main()
