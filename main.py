import sys
from os import path
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pg.display.set_caption("Pygame RPG")
        pg.key.set_repeat(200, 100)
        self.clock = pg.time.Clock()
        self.playing = True
        self.player = None
        self.all_sprites = None
        self.camera = None
        self.walls = None
        self.dt = None
        self.map = None
        self.load_data()

    def load_data(self):
        game_folder = path.dirname(__file__)   # same folder as main.py
        self.map = Map(path.join(game_folder, "map2.txt"))

    def new(self):
        # setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "P":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop (self.playing = False -> end game)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    @staticmethod
    def quit():
        pg.quit()
        sys.exit()

    def update(self):
        # update game loop
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIN_WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, WIN_HEIGHT))
        for y in range(0, WIN_HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIN_WIDTH, y))

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # catch all events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()


# create the game
g = Game()
while True:
    g.new()
    g.run()
