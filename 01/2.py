import sys

def main():
    val_list = [int(x) for x in list(sys.stdin)]
    val_set = set(val_list)

    for i in range(len(val_list)):
        for j in range(i + 1, len(val_list)):
            a = val_list[i]
            b = val_list[j]
            c = 2020 - a - b
            if c in val_set:
                print(str(a * b * c))
                return

main()
