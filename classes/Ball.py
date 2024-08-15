import pygame

class Ball:
    def __init__(self, board_tiles: list, pos: tuple[int, int], radius: int, colors=("black", "white"), init_vel=[1,1]):
        self.x, self.y = pos
        self.radius = radius
        self.vel = init_vel
        self.board_tiles = board_tiles
        self.colors = colors

        self.rect = pygame.Rect(self.x, self.y, radius*2, radius*2)
        self.color = colors[0] if self.y > self.x else colors[1]


    def draw(self, display):
        pygame.draw.circle(display, self.color, self.rect.center, self.radius)
        # pygame.draw.rect(display, "green", self.rect)


    def update(self, display):
        collided_tile = self.check_collisions()
        if collided_tile:
            self.handle_collision(collided_tile)

        self.x += self.vel[0]
        self.y += self.vel[1]

        self.rect.x, self.rect.y = self.x, self.y
        self.draw(display)
    

    def check_collisions(self):
        for tile in self.board_tiles:
            if tile.color == self.color or tile.is_boundary:
                if self.rect.colliderect(tile):
                    return tile
            

    def handle_collision(self, tile):
        left = (self.rect.left+2 >= tile.rect.right)
        right = (self.rect.right-2 <= tile.rect.left)
        top = (self.rect.top+2 >= tile.rect.bottom)
        bottom = (self.rect.bottom-2 <= tile.rect.top)
        # print("left", left, "right", right, "top", top, "bottom", bottom)

        if left or right:
            self.vel[0] = -self.vel[0]
        if top or bottom:
            self.vel[1] = -self.vel[1]

        if not tile.is_boundary:
            tile.color = self.colors[0] if tile.color == self.colors[1] else self.colors[1]
