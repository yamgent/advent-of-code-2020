def main():
    depart = int(input())
    buses = [int(x) for x in filter(lambda x: x != 'x', [x for x in input().split(',')])]
    next_time = [[x, x - (depart % x) if (depart % x) != 0 else 0] for x in buses]
    best = min(next_time, key=lambda x: x[1])
    print(str(best[0] * best[1]))


main()
