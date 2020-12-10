import sys

def main():
    vals = [0] + sorted([int(x.strip()) for x in sys.stdin])
    vals.append(vals[-1] + 3)
    total = len(vals)

    paths = [0] * total
    paths[total - 1] = 1
    for i in range(total - 2, -1, -1):
        for j in range(1, 4):
            if i + j < total and vals[i + j] - vals[i] <= 3:
                paths[i] += paths[i + j]
            else:
                break

    print(paths[0])

main()
