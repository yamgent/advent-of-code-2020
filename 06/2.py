def main():
    count = 0
    group = None

    try:
        while True:
            cur = {x for x in input()}
            if len(cur) > 0:
                if group == None:
                    group = cur
                else:
                    group &= cur
            else:
                count += len(group)
                group = None
    except EOFError:
        count += len(group)

    print(count)


main()
