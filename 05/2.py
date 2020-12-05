import sys

def get_id(pass_str):
    pass_bin = pass_str.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    r = int(pass_bin[:7], 2)
    c = int(pass_bin[7:], 2)
    return r * 8 + c


def main():
    ids = {get_id(p.strip()) for p in sys.stdin}
    low, high = min(ids), max(ids)
    for i in range(low, high):
        if i not in ids:
            print(i)
            return

main()
