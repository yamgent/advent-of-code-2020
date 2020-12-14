import re
import sys

MASK_SET_RE = re.compile(r"mask = ([01X]+)")
MEM_SET_RE = re.compile(r"mem\[(\d+)] = (\d+)")

def and_mask(value, mask):
    assert len(value) == len(mask)

    final = []
    for i in range(len(value)):
        if mask[i] == '0':
            final.append(value[i])
        else:
            final.append(mask[i])

    return ''.join(final)

def main():
    mask = ''
    mask_X_pos = 0
    mem = {}

    for l in sys.stdin:
        if l.startswith('mask'):
            mask = MASK_SET_RE.match(l).group(1)
            mask_X_pos = [x[0] for x in enumerate(list(mask)) if x[1] == 'X']
            mask_X_pos.reverse()
        elif l.startswith('mem'):
            loc_mask, val = MEM_SET_RE.match(l).groups()
            loc_mask = and_mask(format(int(loc_mask), '036b'), mask)
            val = int(val)
            for i in range(pow(2, len(mask_X_pos))):
                loc = list(loc_mask)
                for j in range(len(mask_X_pos)):
                    loc[mask_X_pos[j]] = '1' if (i & (1 << j)) else '0'
                loc = ''.join(loc)
                loc = int(loc, 2)
                mem[loc] = val
        else:
            raise ValueError()

    print(sum(mem.values()))

main()
