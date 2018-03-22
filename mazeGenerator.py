# Modular Programming!
from pygame import *
from random import *

init()
dimensions = (800, 800)  # TUPLE - same as list or array but cannot be editted
screen = display.set_mode((dimensions[0]+300,dimensions[1]))
display.set_caption("Pygame Week 1")

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def createMaze():
    screen.fill(WHITE)
    createBorders()
    createInsides()
    drawControls()
    display.flip()


def createBorders():
    # Left border
    draw.line(screen, BLACK, (0, 0), (0, dimensions[1]), 20)
    # Right border
    draw.line(screen, BLACK, (dimensions[0], 0), (dimensions[0], dimensions[1]), 20)
    # Top border
    draw.line(screen, BLACK, (0, 0), (dimensions[0], 0), 20)
    # Bottom Border
    draw.line(screen, BLACK, (0, dimensions[1]), (dimensions[0], dimensions[1]), 20)


def createInsides():
    for x in range(10, dimensions[0] - 10, 10):
        for y in range(10, dimensions[1] - 10, 10):
            orientation = randint(1, 4)
            if orientation == 1:
                leftPiece(x, y)
            elif orientation == 2:
                rightPiece(x, y)
            if orientation == 3:
                topPiece(x, y)
            if orientation == 4:
                bottomPiece(x, y)


def leftPiece(x, y):
    draw.line(screen, BLACK, (x, y), (x, y + 10))


def rightPiece(x, y):
    draw.line(screen, BLACK, (x + 10, y), (x + 10, y + 10))


def topPiece(x, y):
    draw.line(screen, BLACK, (x, y), (x + 10, y))


def bottomPiece(x, y):
    draw.line(screen, BLACK, (x, y + 10), (x + 10, y + 10))

def drawControls():
    drawNext()
    drawQuit()

def drawNext():
    print()

def drawQuit():
    print()




breaker = False
while not breaker:
    for e in event.get():
        if e.type == QUIT:
            breaker = True
    x = input("Press enter to create another maze:")
    createMaze()
    if x == "quit":
        breaker = True

quit()
