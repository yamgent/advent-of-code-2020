import sys

def main():
    vals = {int(x) for x in list(sys.stdin)}
    for v in vals:
        w = 2020 - v
        if w in vals:
            print(str(v * w))
            return

main()
