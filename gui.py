import random
import pygame
pygame.font.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
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
        rect = pygame.Rect(OFFSET, OFFSET, WINDOW_WIDTH-2*OFFSET, WINDOW_HEIGHT-2*OFFSET)
        pygame.draw.rect(win, self.BG_COLOR, rect)


class Pellet():
    def __init__(self):
        pass

    def draw(self):
        pass


class Cell():
    RADIUS = 4
    VEL = 0.01


    def __init__(self):
        self.x = random.random()
        self.y = random.random()
        self.col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rad = 1

    def draw(self, win):
        pygame.draw.circle(win, self.col, (int(self.x*(WINDOW_WIDTH-2*OFFSET)+OFFSET), int(self.y*(WINDOW_HEIGHT-2*OFFSET)+OFFSET)), self.rad*self.RADIUS)

    def move(self, left, up, right, down):
        self.x = self.x + right*self.VEL
        self.x = self.x - left*self.VEL
        self.y = self.y + down*self.VEL
        self.y = self.y - up*self.VEL

class Virus():
    def __init__(self, col):
        self.col = col # red or green

    def draw(self):
        pass




def draw_window(win, board, cells):            
    board.draw(win)
    for cell in cells:
        cell.draw(win)

    pygame.display.update()


def main():
    global WIN
    win = WIN

    clock = pygame.time.Clock()

    board = Board()
    mycell = Cell()
    cells = [mycell]

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            mycell.move(1, 0, 0, 0)
        if keys[pygame.K_UP]:
            mycell.move(0, 1, 0, 0)
        if keys[pygame.K_RIGHT]:
            mycell.move(0, 0, 1, 0)
        if keys[pygame.K_DOWN]:
            mycell.move(0, 0, 0, 1)


            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         mycell.move(1, 0, 0, 0)
            #     if event.key == pygame.K_UP:
            #         mycell.move(0, 1, 0, 0)
            #     if event.key == pygame.K_RIGHT:
            #         mycell.move(0, 0, 1, 0)
            #     if event.key == pygame.K_DOWN:
            #         mycell.move(0, 0, 0, 1)

        draw_window(win, board, cells)


if __name__ == '__main__':
    main()