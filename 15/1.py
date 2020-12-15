def main():
    last_seen = {num: idx + 1 for idx, num in enumerate([int(x) for x in input().split(',')])}
    last_spoke = 0
    turn = len(last_seen) + 2

    while turn != 2021:
        if last_spoke in last_seen:
            new = (turn - 1) - last_seen[last_spoke]
        else:
            new = 0

        last_seen[last_spoke] = turn - 1
        last_spoke = new
        turn += 1

    print(last_spoke)

main()
