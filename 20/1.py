W, H = 10, 10


# get a unique edge ID for a particular edge
def gen_edge_uid(pix):
    # go from left to right
    ltr = 0
    cur = 1
    for i in range(len(pix) - 1, -1, -1):
        if pix[i] == '#':
            ltr += cur
        cur *= 2

    # go from right to left
    rtl = 0
    cur = 1
    for i in range(len(pix)):
        if pix[i] == '#':
            rtl += cur
        cur *= 2

    # always get the smaller of the two
    # which guarantees uniqueness
    return min(ltr, rtl)


class Tile:
    def __init__(self, tid, pixels):
        self.tid = tid
        self.pixels = pixels

        top_id = gen_edge_uid(list(pixels[0]))
        bot_id = gen_edge_uid(list(pixels[H - 1]))
        left_id = gen_edge_uid([pixels[i][0] for i in range(len(pixels))])
        right_id = gen_edge_uid([pixels[i][W - 1] for i in range(len(pixels))])
        self.edge_uids = [top_id, bot_id, left_id, right_id]


def main():
    tiles = {}

    try:
        while True:
            header = input()
            tid = int(header.split(' ')[1][:-1])
            pixels = [input() for x in range(H)]
            tiles[tid] = Tile(tid, pixels)

            # discard blank line
            input()

    except EOFError:
        pass

    common_edges = {}
    for tid in tiles:
        for edge in tiles[tid].edge_uids:
            if edge not in common_edges:
                common_edges[edge] = []
            common_edges[edge].append(tid)

    corner_tids = 1
    for tid in tiles:
        isolated = 0
        for edge in tiles[tid].edge_uids:
            if len(common_edges[edge]) == 1:
                isolated += 1
        if isolated == 2:
            corner_tids *= tid

    print(corner_tids)


main()
