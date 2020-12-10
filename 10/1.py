import sys

def main():
    vals = [0] + sorted([int(x.strip()) for x in sys.stdin])
    vals.append(vals[-1] + 3)

    diff1 = 0
    diff3 = 0
    for i in range(1, len(vals)):
        d = vals[i] - vals[i-1]
        if d == 1:
            diff1 += 1
        elif d == 3:
            diff3 += 1

    print(str(diff1 * diff3))


main()
