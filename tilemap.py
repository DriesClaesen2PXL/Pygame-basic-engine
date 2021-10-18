import pygame as pg
from config import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, "rt") as f:
            for line in f:
                self.data.append(line.strip())  # strip newline character

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILE_SIZE
        self.height = self.tileheight * TILE_SIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIN_WIDTH/2)
        y = -target.rect.y + int(WIN_HEIGHT/2)

        # limit scrolling to map size
        x = min(0, x)   # left
        y = min(0, y)   # top
        x = max(-(self.width - WIN_WIDTH), x)   # right
        y = max(-(self.height - WIN_HEIGHT), y)   # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
