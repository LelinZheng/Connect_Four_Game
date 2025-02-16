from constant import MAX_GRID_SIZE, COL_0_X, COL_SPACE, COL
import random


class ComputerPlayer:
    """A computer ai player deciding where to place the yellow circles"""
    def __init__(self, grid, endgame):
        self.grid = grid
        self.endgame = endgame
        self.COL_X_LIST = [COL_0_X + x * COL_SPACE for x in range(COL)]

    def x_to_place(self):
        """Returns x value for the circle"""
        if self.almost_win() != -1:
            return self.almost_win()

        if self.stop_win() != -1:
            return self.stop_win()

        while not self.endgame:
            i = random.randint(0, len(self.grid)-1)
            if len(self.grid[i]) < MAX_GRID_SIZE:
                return self.COL_X_LIST[i]
        return -1

    def stop_win(self):
        """Try to find if the opponent has 3 in a row/col and stop that"""
        def is_valid(i, j):
            """Check if i and j in grid[i] exists"""
            if i >= 0 and len(self.grid) > i and \
               len(self.grid[i]) > j and j >= 0:
                return True
            return False

        num_of_red = 0
        # check last 3 circles in the column
        for i in range(len(self.grid)):
            num_of_red = 0
            length = len(self.grid[i])
            for j in range(length-3, length):
                if is_valid(i, j):
                    if self.grid[i][j] == 1:
                        num_of_red += 1
                    else:
                        num_of_red = 0
                    if num_of_red == 3 and \
                       len(self.grid[i]) <= MAX_GRID_SIZE-1:
                        return self.COL_X_LIST[i]

        num_of_red = 0
        # check circles in the row
        for j in range(MAX_GRID_SIZE):
            num_of_red = 0
            start_i = 0  # continuous red from this i index
            for i in range(len(self.grid)):
                if is_valid(i, j) and self.grid[i][j] == 1:
                    num_of_red += 1
                else:
                    num_of_red = 0
                    start_i = i+1 if i+1 < len(self.grid) else -1

                # it will stop for 2 or 3 red in a row
                if num_of_red == 3 or num_of_red == 2:
                    # if the next col could just add 1 yellow to stop win
                    if j == 0 and i+1 < len(self.grid) and \
                     not is_valid(i+1, j):
                        # when there is no other ones in i+1 col
                        return self.COL_X_LIST[i+1]
                    elif is_valid(i+1, j-1) and not is_valid(i+1, j):
                        # if the i+1 col could just add 1 yellow to stop win
                        return self.COL_X_LIST[i+1]
                    elif j == 0 and start_i-1 >= 0 and \
                            not is_valid(start_i-1, j):
                        # when there is no other ones in start_i-1 col
                        return self.COL_X_LIST[start_i-1]
                    elif is_valid(start_i-1, j-1) and \
                            not is_valid(start_i-1, j):
                        # if the i+1 col could just add 1 yellow to stop win
                        return self.COL_X_LIST[start_i-1]
        return -1

    def almost_win(self):
        """Try to win if 3 yellows in a col/row"""

        def is_valid(i, j):
            """Check if i and j in grid[i] exists"""
            if i >= 0 and len(self.grid) > i and len(self.grid[i]) > j \
               and j >= 0:
                return True
            return False

        num_of_yellow = 0
        # check last 3 circles in the column
        for i in range(len(self.grid)):
            num_of_yellow = 0
            length = len(self.grid[i])
            for j in range(length-3, length):
                if is_valid(i, j):
                    if self.grid[i][j] == -1:
                        num_of_yellow += 1
                    else:
                        num_of_yellow = 0
                    if num_of_yellow == 3 and \
                       len(self.grid[i]) <= MAX_GRID_SIZE-1:
                        return self.COL_X_LIST[i]

        num_of_yellow = 0
        # check circles in the row
        for j in range(MAX_GRID_SIZE):
            num_of_yellow = 0
            start_i = 0
            for i in range(len(self.grid)):
                if is_valid(i, j) and self.grid[i][j] == -1:
                    num_of_yellow += 1
                else:
                    num_of_yellow = 0
                    start_i = i+1 if i+1 < len(self.grid) else -1

                if num_of_yellow == 3:
                    if j == 0 and i+1 < len(self.grid) and \
                       not is_valid(i+1, j):
                        return self.COL_X_LIST[i+1]
                    elif is_valid(i+1, j-1) and not is_valid(i+1, j):
                        return self.COL_X_LIST[i+1]
                    elif j == 0 and start_i-1 >= 0 and \
                            not is_valid(start_i-1, j):
                        return self.COL_X_LIST[start_i-1]
                    elif is_valid(start_i-1, j-1) and \
                            not is_valid(start_i-1, j):
                        return self.COL_X_LIST[start_i-1]
        return -1
