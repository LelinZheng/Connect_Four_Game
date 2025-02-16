from circle import Circle
from stack import Stack
from message import Message
from computer_player import ComputerPlayer
import constant


class Game_Controller:
    """Manage the game flow"""

    def __init__(self):
        self.TOP_SPACE_Y = constant.TOP_SPACE_Y
        self.CIRC_RADIUS = constant.CIRC_RADIUS
        self.ROW_THICK = constant.ROW_THICK
        self.COL = constant.COL
        self.ROW = constant.ROW
        self.COL_SPACE = constant.COL_SPACE
        self.COL_0_X = constant.COL_0_X

        self.WIDTH = constant.WIDTH
        self.HEIGHT = constant.HEIGHT
        self.MAX_GRID_SIZE = constant.MAX_GRID_SIZE

        self.to_draw = Stack()
        self.turn = 1  # player(red) is 1, red goes first
        self.is_dropping = False
        self.can_drop = False  # if the circle reachs the target bottom
        self.grid = [[] for _ in range(constant.COL)]  # populating the col
        self.endgame = False
        self.player_win = False
        self.comp_win = False
        self.is_filled = False

        self.comp_delay_set = False
        self.comp_delay_start = 0
        self.comp_delay_duration = 1000  # delay in milliseconds

        self.scoring_delay_set = False
        self.scoring_delay_start = 0
        self.scoring_delay_duration = 500

        self.COL_X_LIST = [constant.COL_0_X +
                           x * constant.COL_SPACE for x in range(constant.COL)]

        self.TARGET_Y_LIST = [constant.HEIGHT - constant.CIRC_RADIUS -
                              constant.COL_SPACE * x - constant.ROW_THICK
                              for x in range(constant.ROW)]

        self.message = Message("Player's turn", "RED")  # Default message

    def update(self):
        """update the gameboard in the draw() function"""
        if self.is_dropping:
            self.dropping()  # refresh the dropping circle loc

        for circle in self.to_draw.contents:
            circle.display()

        if self.filled_board():
            self.endgame = True

        self.message.display()

        if self.turn == -1 and not self.is_dropping and not self.endgame:
            if not self.comp_delay_set:
                self.comp_delay_set = True
                self.comp_delay_start = millis()

            # Delay computer action
            if millis() >= self.comp_delay_start + self.comp_delay_duration:
                computer = ComputerPlayer(self.grid, self.endgame)
                computer_x = computer.x_to_place()
                if computer_x != -1:  # handle when there is no x returned
                    self.to_draw.push(Circle(computer_x, self.TOP_SPACE_Y//2,
                                      self.turn))
                    self.computer_circ_dropping(computer_x,
                                                self.TOP_SPACE_Y//2)
                self.comp_delay_set = False

        stroke(0, 0, 200)
        strokeWeight(self.ROW_THICK)

        # drawing the grid
        for row in range(1, self.ROW+2):
            y = self.COL_SPACE * row
            line(0, y, self.WIDTH, y)

        for col in range(0, self.COL+2):
            x = self.COL_SPACE * col
            line(x, self.COL_SPACE, x, self.HEIGHT)

        # Delay scoring window from popping up too soon
        if self.scoring_delay_set and \
           millis() >= self.scoring_delay_start + self.scoring_delay_duration:
            self.score()
            self.scoring_delay_set = False

    def updateMessage(self):
        """update the endgame message and calling turns"""
        if self.filled_board() and not self.comp_win and not self.player_win:
            self.message = Message("Game Over!", "BLACK")
        elif self.player_win:
            self.message = Message("Player Win! Game Over!", "RED")
            self.scoring_delay_set = True
            self.scoring_delay_start = millis()
            # Schedule score() to run after 500 ms
        elif self.comp_win:
            self.message = Message("Computer Win! Game Over!", "BLACK")
        else:
            self.callingTurns()

    def mousePressed_update(self, mouseX, mouseY):
        """Show cicles at the top space when mousePressed in player's turn"""
        if not self.endgame and self.turn == 1:
            if (not self.is_dropping) and mouseY < self.TOP_SPACE_Y:
                for i, col_x in enumerate(self.COL_X_LIST):
                    if abs(col_x - mouseX) < self.COL_SPACE//2 and\
                       self.havespace(i):
                        if self.turn == 1:
                            self.to_draw.push(Circle(col_x,
                                              self.TOP_SPACE_Y//2, self.turn))

    def mouseReleased_update(self, mouseX, mouseY):
        """Enable dropping cicles when mouseReleased in player's turn"""
        # remove the circle at the top space
        if not self.endgame and self.turn == 1:
            if not self.is_dropping:
                circle = self.to_draw.peek()
                if circle:
                    col_x = circle.x
                    col_y = circle.y
                    if col_y == self.TOP_SPACE_Y//2:
                        self.to_draw.pop()

            # If mouse released within the top space and the column, it drops
            if (not self.is_dropping) and (mouseY < self.TOP_SPACE_Y) and\
               (abs(col_x - mouseX) < self.COL_SPACE//2):
                for i, column_x in enumerate(self.COL_X_LIST):
                    if col_x == column_x and self.havespace(i):
                        self.grid[i].append(1)  # red ones
                        self.to_draw.push(Circle(col_x, self.TOP_SPACE_Y//2,
                                                 self.turn))
                        self.can_drop = True
                        self.is_dropping = True

    def computer_circ_dropping(self, x, y):
        """Enabled dropping in computer's turn"""
        # remove the circle at the top space
        if not self.endgame:
            if not self.is_dropping:
                circle = self.to_draw.peek()
                if circle:
                    col_x = circle.x
                    col_y = circle.y
                    if col_y == self.TOP_SPACE_Y//2:
                        self.to_draw.pop()

                for i, column_x in enumerate(self.COL_X_LIST):
                    if col_x == column_x:
                        self.grid[i].append(-1)  # yellow ones
                        self.to_draw.push(Circle(col_x, self.TOP_SPACE_Y//2,
                                          self.turn))
                        self.can_drop = True
                        self.is_dropping = True

    def dropping(self):
        """displaying the dropping circle in action """
        DROP_SPEED = 20
        if self.to_draw.is_empty():  # if there isn't any circle in the stack
            self.is_dropping = False
            return

        # getting the last circle to drop
        dropping_circle = self.to_draw.peek()
        dropping_circle.y += DROP_SPEED
        x = dropping_circle.x

        # To track which col should the circle drop into
        for i, col_x in enumerate(self.COL_X_LIST):
            if col_x == x:
                num_in_col = len(self.grid[i])
                if dropping_circle.y >= self.TARGET_Y_LIST[num_in_col-1]:
                    if self.is_winning(i, len(self.grid[i])-1,
                                       dropping_circle.turn):
                        if dropping_circle.turn == 1:
                            self.player_win = True
                        elif dropping_circle.turn == -1:
                            self.comp_win = True
                        self.endgame = True
                    self.turn = - self.turn
                    self.is_dropping = False
                    self.can_drop = False
                    self.updateMessage()

    def havespace(self, i):
        """To check if there is space in the column for circles to drop"""
        if len(self.grid[i]) >= self.MAX_GRID_SIZE:
            return False
        else:
            return True

    def filled_board(self):
        """To check if the board is filled -> Boolean"""
        for i in range(len(self.grid)):
            if self.havespace(i):
                return self.is_filled
        self.is_filled = True
        return self.is_filled

    def callingTurns(self):
        """Calling turns"""
        if self.turn == 1:
            self.message = Message("Player's turn", "RED")
        elif self.turn == -1:
            self.message = Message("Computer's turn", "YELLOW")

    def is_winning(self, col_i, row_j, color):
        """Checks if th game has a winner"""

        def is_valid(i, j):
            """Check if i and j in grid[i] exists"""
            if i >= 0 and len(self.grid) > i and len(self.grid[i]) > j and\
               j >= 0:
                return True
            return False

        numofcolor = 0
        # check circles in the column 
        for j in range(len(self.grid[col_i])):
            if self.grid[col_i][j] == color:
                numofcolor += 1
            else:
                numofcolor = 0
            if numofcolor == 4:
                return True

        numofcolor = 0
        # check circles in the row
        for i in range(len(self.grid)):
            if is_valid(i, row_j) and self.grid[i][row_j] == color:
                numofcolor += 1
            else:
                numofcolor = 0
            if numofcolor == 4:
                return True

        # check diagonally
        numofcolor = 0
        for k in range(-3, 4):
            if is_valid(col_i+k, row_j+k) and\
               self.grid[col_i+k][row_j+k] == color:
                numofcolor += 1
            else:
                numofcolor = 0
            if numofcolor == 4:
                return True

        numofcolor = 0
        for k in range(-3, 4):
            if is_valid(col_i+k, row_j-k) and\
               self.grid[col_i+k][row_j-k] == color:
                numofcolor += 1
            else:
                numofcolor = 0
            if numofcolor == 4:
                return True

    def score(self):
        def input(message=''):
            """Defines the input function"""
            from javax.swing import JOptionPane
            return JOptionPane.showInputDialog(frame, message)

        def saveScores(name):
            """Saving score in score.txt"""

            def read_file():
                with open('scores.txt', "r") as file:
                    lines = file.readlines()
                return lines

            lines = read_file()
            list_of_scores = []
            is_existing_name = False

            for line in lines:
                words = line.split(" ")
                # handle when player name has space
                if len(words) > 2:
                    player = " ".join(words[0:len(words)-1])
                else:
                    player = words[0]

                if name == player:  # if the name exists
                    score = int(words[-1])
                    score += 1
                    list_of_scores.append([player, score])
                    is_existing_name = True
                else:
                    list_of_scores.append([player, int(words[-1])])
                    # making a copy of the scores

            if not is_existing_name:
                list_of_scores.append([name, 1])

            list_of_scores.sort(key=lambda x: x[-1], reverse=True)
            # sort the list

            with open('scores.txt', 'w') as file:
                for score in list_of_scores:
                    file.write(score[0] + " " + str(score[1]) + '\n')

        answer = str(input('enter your name')).strip()

        if answer and answer != "None":
            saveScores(answer)
