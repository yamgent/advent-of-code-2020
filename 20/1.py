def gen_edge_uid(pix):
    # left to right
    ltr = 0
    cur = 1
    for i in range(len(pix) - 1, -1, -1):
        if pix[i] == '#':
            ltr += cur
        cur *= 2

    # right to left
    rtl = 0
    cur = 1
    for i in range(len(pix)):
        if pix[i] == '#':
            rtl += cur
        cur *= 2

    return min(ltr, rtl)


def main():
    W, H = 10, 10

    tiles = {}

    try:
        while True:
            header = input()
            tid = int(header.split(' ')[1][:-1])

            pixels = []
            while len(pixels) != H:
                pixels.append(input())

            top_id = gen_edge_uid(list(pixels[0]))
            bot_id = gen_edge_uid(list(pixels[H - 1]))
            left_id = gen_edge_uid([pixels[i][0] for i in range(len(pixels))])
            right_id = gen_edge_uid([pixels[i][W - 1] for i in range(len(pixels))])
            tiles[tid] = [top_id, bot_id, left_id, right_id]

            # discard blank line
            input()

    except EOFError:
        pass


    common_edges = {}
    for tid in tiles:
        for edge in tiles[tid]:
            if edge not in common_edges:
                common_edges[edge] = []
            common_edges[edge].append(tid)

    corner_tids = 1
    for tid in tiles:
        isolated = 0
        for edge in tiles[tid]:
            if len(common_edges[edge]) == 1:
                isolated += 1
        if isolated == 2:
            corner_tids *= tid

    print(corner_tids)


main()
