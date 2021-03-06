import random
import pygame
import numpy as np

pygame.font.init()

WINDOW_HEIGHT = 900
WINDOW_WIDTH = int(WINDOW_HEIGHT * 16 / 9)
WINDOW_WIDTH = WINDOW_HEIGHT

FPS = 30
OFFSET = 20

FONT = pygame.font.SysFont("arial", 20)

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Agario")


class Board:
    BG_COLOR = (255, 255, 0)

    def __init__(self):
        pass

    def draw(self, win):
        rect = pygame.Rect(
            OFFSET, OFFSET, WINDOW_WIDTH - 2 * OFFSET, WINDOW_HEIGHT - 2 * OFFSET
        )
        pygame.draw.rect(win, self.BG_COLOR, rect)


class Cell:
    RADIUS = 4
    VEL = 0.01

    def __init__(self):
        self.position = np.random.random(2)
        self.col = np.random.randint(0, 256, 3)
        self.rad = 1

    def draw(self, win):
        pygame.draw.circle(
            win,
            self.col,
            (
                int(self.position[0] * (WINDOW_WIDTH - 2 * OFFSET) + OFFSET),
                int(self.position[1] * (WINDOW_HEIGHT - 2 * OFFSET) + OFFSET),
            ),
            self.rad * self.RADIUS,
        )

    def move(self, translation):
        self.position = self.position + np.array(translation) * self.VEL

    def eat(self, other):
        self.rad = np.sqrt(self.rad ** 2 + other.rad ** 2)


class Pellet(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Pellet"


class Virus(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Virus"
        self.color = random.choice([(152, 189, 27), (223, 92, 27)])


class Player(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Player"
        self.RADIUS = 5


def draw_window(win, board, cells):
    board.draw(win)
    for cell in cells:
        cell.draw(win)

    pygame.display.update()


def eattime(players, pallets, viruses):
    _players, _pallets, _viruses = [], [], []
    for p in range(len(players)):
        for pal in range(len(pallets)):
            abstand = np.linalg.norm(players[p].position - pallets[pal].position)
            print(abstand)
            if np.linalg.norm(players[p].position - pallets[pal].position) > 0.01:
                _pallets.append(pallets[pal])
            else:
                players[p].rad += pallets[pal].rad

    return [players, _pallets, viruses]


def main():
    global WIN
    win = WIN
    MaxPallets = 5

    clock = pygame.time.Clock()

    board = Board()
    mycell = Player()
    players = [mycell]
    pallets = [Pellet()]
    viruses = []
    run = True
    while run:
        if random.random() > 0.96 and len(pallets) < MaxPallets:  #
            pallets.append(Pellet())
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mycell.move([-1, 0])
        if keys[pygame.K_UP]:
            mycell.move([0, -1])
        if keys[pygame.K_RIGHT]:
            mycell.move([1, 0])
        if keys[pygame.K_DOWN]:
            mycell.move([0, 1])
        players, pallets, viruses = eattime(players, pallets, viruses)

        draw_window(win, board, [*players, *pallets, *viruses])


if __name__ == "__main__":
    main()
