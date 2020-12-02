import sys

def main():
    vals = set([int(x) for x in list(sys.stdin)])
    for v in vals:
        if 2020 - v in vals:
            print(str(v * (2020 - v)))
            return

main()
