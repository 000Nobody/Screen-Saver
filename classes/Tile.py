import pygame

class Tile:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], boundary_tile=False, colors=("black", "white")):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.is_boundary = boundary_tile

        self.color = colors[0] if pos[1] < pos[0] else colors[1]


    def draw(self, display):
        pygame.draw.rect(display, self.color, self.rect)

    