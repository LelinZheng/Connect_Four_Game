from constant import CIRC_RADIUS


class Circle:
    """Class for drawing yellow and red circles"""
    def __init__(self, x, y, turn):
        self.x = x
        self.y = y
        self.turn = turn
        self.DIAMETER = CIRC_RADIUS * 2

    def display(self):
        if self.turn == 1:
            self.red_circle()
        elif self.turn == -1:
            self.yellow_circle()

    def yellow_circle(self):
        noStroke()
        fill(200, 200, 0)
        circle(self.x, self.y, self.DIAMETER)

    def red_circle(self):
        noStroke()
        fill(200, 0, 0)
        circle(self.x, self.y, self.DIAMETER)
