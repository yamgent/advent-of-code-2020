# good for test cases, but takes too long for actual input

def main():
    depart = int(input())
    buses = list(enumerate([int(x) if x != 'x' else 0 for x in input().split(',')]))
    biggest = max(buses, key=lambda x: x[1])
    i = 0
    while True:
        i += 1
        time = (biggest[1] * i) - biggest[0]
        if all([(time + x[0]) % x[1] == 0 if x[1] != 0 else True for x in buses]):
            print(time)
            return


main()
