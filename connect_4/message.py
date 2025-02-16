from constant import WIDTH, TOP_SPACE_Y, TEXT_SIZE


class Message:
    """Class for displaying message"""
    def __init__(self, string, color):
        self.x = WIDTH/2
        self.y = TOP_SPACE_Y/2
        self.string = string
        self.color = color

    def display(self):
        textAlign(CENTER);
        textSize(TEXT_SIZE)
        if self.color.upper() == "RED":
            fill(100, 0, 0)
        elif self.color.upper() == "YELLOW":
            fill(200, 200, 0)
        elif self.color.upper() == "BLACK":
            fill(0, 0, 0)

        text(self.string, self.x, self.y)
