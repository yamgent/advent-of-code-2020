MAX = 9

def main():
    cups = [int(x) for x in input()]

    for moves in range(100):
        current = cups[0]

        # pick up
        pick_up = cups[1:4]
        cups = [cups[0]] + cups[4:]

        # select dest
        dest = current - 1 if current - 1 > 0 else MAX
        while dest not in cups:
            dest = dest - 1 if dest - 1 > 0 else MAX

        # place cups
        insert_idx = cups.index(dest) + 1
        cups = cups[0:insert_idx] + pick_up + cups[insert_idx:]

        # new cup
        cups = cups[1:] + [cups[0]]

    while cups[0] != 1:
        cups = cups[1:] + [cups[0]]

    print(''.join([str(x) for x in cups[1:]]))

main()
