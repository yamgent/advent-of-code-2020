W, H = 10, 10


# get a unique edge ID for a particular edge
def gen_edge_uid(pix):
    binary = ['0' if x == '.' else '1' for x in pix]

    # standard order
    normal = int(''.join(binary), 2)
    # flipped
    flipped = int(''.join(reversed(binary)), 2)

    # always get the smaller of the two
    # which guarantees uniqueness for same edges
    # in different orientation
    return min(normal, flipped)


# represents a single tile. Edge order: T, R, B, L
class Tile:
    def __init__(self, tid, pixels):
        self.tid = tid
        self.pixels = pixels

        top_id = gen_edge_uid(list(pixels[0]))
        bot_id = gen_edge_uid(list(pixels[H - 1]))
        left_id = gen_edge_uid([pixels[i][0] for i in range(len(pixels))])
        right_id = gen_edge_uid([pixels[i][W - 1] for i in range(len(pixels))])
        self.edge_uids = [top_id, right_id, bot_id, left_id]
        self.edge_tiles = [None] * 4

    def __repr__(self):
        return 'Tile(tid={}, pixels=[..], edge_uids={}, edge_tiles={})'.format(
            self.tid, self.edge_uids, [t.tid if t is not None else 'None' for t in self.edge_tiles])


# parse input
def parse_input():
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

    return tiles


# connect tiles to each other that shares the same edge
# edge comparison can be done using the unique edge ids
def connect_tiles(tiles):
    common_edges = {}
    for tid, tile in tiles.items():
        for edge in tile.edge_uids:
            if edge not in common_edges:
                common_edges[edge] = []
            common_edges[edge].append(tid)

    for tid, tile in tiles.items():
        for i, edge in enumerate(tile.edge_uids):
            # assume that one edge will match at most two tiles
            if len(common_edges[edge]) == 2:
                other_tid = common_edges[edge][0]
                if other_tid == tid:
                    other_tid = common_edges[edge][1]
                tile.edge_tiles[i] = tiles[other_tid]


NEXT_EDGE_CHANGE = [2, 3, 0, 1]

def traverse(start_tile, edge_tile_idx):
    res = [start_tile]
    prev = start_tile
    cur = start_tile.edge_tiles[edge_tile_idx]

    while cur is not None:
        cur_edge_idx = cur.edge_tiles.index(prev)
        next_edge_idx = NEXT_EDGE_CHANGE[cur_edge_idx]

        res.append(cur)
        prev = cur
        cur = cur.edge_tiles[next_edge_idx]

    return res


# generate the layout given the connected tiles
def generate_layout(tiles):
    # find any corner tiles
    corner = [tile for tid, tile in tiles.items() if tile.edge_tiles.count(None) == 2][0]
    left_column_tiles = traverse(corner, 0 if corner.edge_tiles[0] != None else 2)

    rows = []
    for tile in left_column_tiles:
        neighbour_idx = [i for i, edge_tile in enumerate(tile.edge_tiles)
            if edge_tile not in left_column_tiles and edge_tile is not None][0]
        rows.append(traverse(tile, neighbour_idx))

    return rows


# degrees are in CW direction
ORI_NORM = 0
ORI_90 = 1
ORI_180 = 2
ORI_270 = 3
ORI_FLIP = 4     # flip on x axis
ORI_FLIP_90 = 5
ORI_FLIP_180 = 6
ORI_FLIP_270 = 7

# rotate CW 90 degrees
def rotate_edge_tiles(edge_tiles):
    return [edge_tiles[-1]] + edge_tiles[:-1]


# get orientation of the pixels given the four neighbour tiles
def get_orientation(layout, y, x):
    # T R B L
    neighbours = [
        None if y - 1 < 0 else layout[y - 1][x],
        None if x + 1 >= len(layout[y]) else layout[y][x + 1],
        None if y + 1 >= len(layout) else layout[y + 1][x],
        None if x - 1 < 0 else layout[y][x - 1]
        ]
    cur = list(layout[y][x].edge_tiles)

    if neighbours == cur:
        return ORI_NORM

    cur = rotate_edge_tiles(cur)
    if neighbours == cur:
        return ORI_90

    cur = rotate_edge_tiles(cur)
    if neighbours == cur:
        return ORI_180

    cur = rotate_edge_tiles(cur)
    if neighbours == cur:
        return ORI_270

    cur = list(layout[y][x].edge_tiles)
    cur[0], cur[2] = cur[2], cur[0]
    if neighbours == cur:
        return ORI_FLIP

    cur = rotate_edge_tiles(cur)
    if neighbours == cur:
        return ORI_FLIP_90

    cur = rotate_edge_tiles(cur)
    if neighbours == cur:
        return ORI_FLIP_180

    cur = rotate_edge_tiles(cur)
    if neighbours == cur:
        return ORI_FLIP_270

    assert False


def rotate_flip_pixels(pixels, orientation):
    H = len(pixels) if orientation in [ORI_NORM, ORI_180, ORI_FLIP, ORI_FLIP_180] else len(pixels[0])
    W = len(pixels[0]) if H != len(pixels[0]) else len(pixels)

    res = []
    for y in range(H):
        row = []
        for x in range(W):
            orig_x = x
            orig_y = y

            if orientation == ORI_90 or orientation == ORI_FLIP_270:
                orig_x = y
                orig_y = len(pixels) - x - 1
            elif orientation == ORI_180 or orientation == ORI_FLIP_180:
                orig_x = len(pixels[0]) - x - 1
                orig_y = len(pixels) - y - 1
            elif orientation == ORI_270 or orientation == ORI_FLIP_90:
                orig_x = len(pixels[0]) - y - 1
                orig_y = x

            row.append(pixels[orig_y][orig_x])

        res.append(row)

    if orientation in [ORI_FLIP, ORI_FLIP_90, ORI_FLIP_180, ORI_FLIP_270]:
        res = list(reversed(res))
    return res


# generate the image given the layout
def generate_image(layout):
    grids = []
    for y in range(len(layout)):
        grid_row = []
        for x in range(len(layout[y])):
            orient = get_orientation(layout, y, x)
            grid_row.append([a[1:-1] for a in rotate_flip_pixels(layout[y][x].pixels, orient)[1:-1]])
        grids.append(grid_row)

    res = []
    for y in range(len(grids)):
        for iy in range(H - 2):
            res_row = []
            for x in range(len(grids[y])):
               for ix in range(W - 2):
                   res_row.append(grids[y][x][iy][ix])
            res.append(res_row)

    return res


# count hashes
def count_hashes(pixels):
    return sum([row.count('#') for row in pixels])


MONSTER = [
    list('                  # '),
    list('#    ##    ##    ###'),
    list(' #  #  #  #  #  #   ')
]

# count monsters
def count_monsters(pixels):
    acc = 0
    for y in range(len(pixels) - len(MONSTER) + 1):
        for x in range(len(pixels[0]) - len(MONSTER[0]) + 1):
            match = True

            for iy in range(len(MONSTER)):
                for ix in range(len(MONSTER[0])):
                    if MONSTER[iy][ix] == ' ':
                        continue
                    if pixels[y + iy][x + ix] != '#':
                        match = False
                        break
                if match == False:
                    break

            if match:
                acc += 1
    return acc


def main():
    tiles = parse_input()
    connect_tiles(tiles)
    layout = generate_layout(tiles)
    image = generate_image(layout)

    # print(tiles)
    # print(layout)
    # print('\n'.join([''.join(row) for row in image]))

    for orient in [ORI_NORM, ORI_90, ORI_180, ORI_270, ORI_FLIP, ORI_FLIP_90, ORI_FLIP_180, ORI_FLIP_270]:
        monsters = count_monsters(rotate_flip_pixels(image, orient))
        if monsters > 0:
            print(str(count_hashes(image) - monsters * count_hashes(MONSTER)))
            return


main()
