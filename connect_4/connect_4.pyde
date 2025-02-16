from game_controller import Game_Controller
"""
A Connect 4 Game for player in red against computer in yellow
"""
gc = Game_Controller()


def setup():
    size(gc.WIDTH, gc.HEIGHT)
    colorMode(RGB, 1)


def draw():
    background(100, 100, 100)
    gc.update()


def mousePressed():
    if mouseButton == LEFT:
        gc.mousePressed_update(mouseX, mouseY)


def mouseReleased():
    if mouseButton == LEFT:
        gc.mouseReleased_update(mouseX, mouseY)
