import re
import sys

MASK_SET_RE = re.compile(r"mask = ([01X]+)")
MEM_SET_RE = re.compile(r"mem\[(\d+)] = (\d+)")

def main():
    or_mask = 0
    and_mask = 0
    mem = {}

    for l in sys.stdin:
        if l.startswith('mask'):
            mask = MASK_SET_RE.match(l).group(1)
            or_mask = int(mask.replace('X', '0'), 2)
            and_mask = int(mask.replace('X', '1'), 2)
        elif l.startswith('mem'):
            loc, val = MEM_SET_RE.match(l).groups()
            mem[loc] = (int(val) | or_mask) & and_mask
        else:
            raise ValueError()

    print(sum(mem.values()))

main()
