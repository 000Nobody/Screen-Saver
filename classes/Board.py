from classes.Tile import Tile

class Board:
    def __init__(self, width: int, height: int, horiz_tiles_num: int, vert_tiles_num: int, colors: tuple):
        self.width = width
        self.height = height
        self.horiz_tiles_num = horiz_tiles_num
        self.vert_tiles_num = vert_tiles_num
        self.colors = colors

        self.tile_width = self.width // horiz_tiles_num
        self.tile_height = self.height // vert_tiles_num
        self.tile_size = (self.tile_width, self.tile_height)

        self.tiles, self.bounds = self.generate_tiles()
        self.flattened_tiles = [j for sub in self.tiles for j in sub]
        self.all_tiles = self.flattened_tiles + self.bounds


    def generate_tiles(self):
        tiles = []
        for y in range(self.vert_tiles_num):
            row = []
            for x in range(self.horiz_tiles_num):
                pos = (x * self.tile_width, y * self.tile_height)
                tile = Tile(pos, self.tile_size, colors=self.colors)
                row.append(tile)
            tiles.append(row)

        bounds = []
        left_bound = Tile((0, 0), (-10, self.height), boundary_tile=True)
        right_bound = Tile((self.width, 0), (10, self.height), boundary_tile=True)
        top_bound = Tile((0, 0), (self.width, -10), boundary_tile=True)
        bottom_bound = Tile((0, self.height), (self.width, 10), boundary_tile=True)
        bounds.extend([left_bound, right_bound, top_bound, bottom_bound])

        return tiles, bounds


    def draw(self, display):
        for row in self.tiles:
            for tile in row:
                tile.draw(display)
