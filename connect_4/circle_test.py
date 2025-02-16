from circle import Circle
from constant import CIRC_RADIUS


def test_constructor():
    x = 0
    y = 1
    turn = 1
    circle = Circle(x, y, turn)
    assert (circle.x == 0 and
            circle.y == 1 and
            circle.turn == 1 and
            circle.DIAMETER == CIRC_RADIUS * 2)
    x = 100
    y = 200
    turn = -1
    circle = Circle(x, y, turn)
    assert (circle.x == 100 and
            circle.y == 200 and
            circle.turn == -1 and
            circle.DIAMETER == CIRC_RADIUS * 2)
