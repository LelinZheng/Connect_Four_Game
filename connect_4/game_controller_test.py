from game_controller import Game_Controller
from circle import Circle
import constant


def test_constructor():
    game_controller = Game_Controller()
    assert (game_controller.TOP_SPACE_Y == constant.TOP_SPACE_Y and
            game_controller.TOP_SPACE_Y == constant.TOP_SPACE_Y and
            game_controller.CIRC_RADIUS == constant.CIRC_RADIUS and
            game_controller.ROW_THICK == constant.ROW_THICK and
            game_controller.COL == constant.COL and
            game_controller.ROW == constant.ROW and
            game_controller.COL_SPACE == constant.COL_SPACE and
            game_controller.COL_0_X == constant.COL_0_X and
            game_controller.WIDTH == constant.WIDTH and
            game_controller.HEIGHT == constant.HEIGHT and
            game_controller.MAX_GRID_SIZE == constant.MAX_GRID_SIZE and
            game_controller.grid == [[] for _ in range(constant.COL)])
    assert (game_controller.turn == 1 and
            not game_controller.is_dropping and
            not game_controller.can_drop and
            not game_controller.endgame and
            not game_controller.player_win and
            not game_controller.comp_win and
            not game_controller.is_filled and
            not game_controller.comp_delay_set and
            not game_controller.scoring_delay_set and
            game_controller.comp_delay_start == 0 and
            game_controller.scoring_delay_start == 0 and
            game_controller.scoring_delay_duration == 500 and
            game_controller.comp_delay_duration == 1000 and
            game_controller.COL_X_LIST == [constant.COL_0_X +
                                           x * constant.COL_SPACE
                                           for x in range(constant.COL)] and
            game_controller.TARGET_Y_LIST == [constant.HEIGHT -
                                              constant.CIRC_RADIUS -
                                              constant.COL_SPACE * x -
                                              constant.ROW_THICK
                                              for x in range(constant.ROW)] and
            game_controller.message.string == "Player's turn" and
            game_controller.message.color == "RED")


def test_mousePressed_update():
    game_controller = Game_Controller()
    mouseX = constant.COL_0_X
    mouseY = constant.TOP_SPACE_Y // 2
    game_controller.mousePressed_update(mouseX, mouseY)
    assert (len(game_controller.to_draw.contents) == 1)
    game_controller = Game_Controller()
    mouseX = game_controller.COL_X_LIST[3]
    mouseY = constant.TOP_SPACE_Y // 2
    game_controller.mousePressed_update(mouseX, mouseY)
    assert (len(game_controller.to_draw.contents) == 1)


def test_mouseReleased_update():
    game_controller = Game_Controller()
    mouseX = constant.COL_0_X
    mouseY = constant.TOP_SPACE_Y // 2
    game_controller.mousePressed_update(mouseX, mouseY)
    game_controller.mouseReleased_update(mouseX, mouseY)
    assert (game_controller.grid[0] == [1] and
            len(game_controller.to_draw.contents) == 1 and
            game_controller.can_drop and
            game_controller.is_dropping)
    game_controller = Game_Controller()
    mouseX = game_controller.COL_X_LIST[3]
    mouseY = constant.TOP_SPACE_Y // 2
    game_controller.mousePressed_update(mouseX, mouseY)
    game_controller.mouseReleased_update(mouseX, mouseY)
    assert (game_controller.grid[3] == [1] and
            len(game_controller.to_draw.contents) == 1 and
            game_controller.can_drop and
            game_controller.is_dropping)


def test_computer_circ_dropping():
    game_controller = Game_Controller()
    game_controller.turn = -1
    x = constant.COL_0_X
    y = constant.TOP_SPACE_Y // 2
    game_controller.to_draw.push(Circle(x, y,
                                        game_controller.turn))
    game_controller.computer_circ_dropping(x, y)
    assert (game_controller.grid[0] == [-1] and
            len(game_controller.to_draw.contents) == 1 and
            game_controller.can_drop and
            game_controller.is_dropping)

    game_controller = Game_Controller()
    game_controller.turn = -1
    x = game_controller.COL_X_LIST[3]
    y = constant.TOP_SPACE_Y // 2
    game_controller.to_draw.push(Circle(x, y,
                                        game_controller.turn))
    game_controller.computer_circ_dropping(x, y)
    assert (game_controller.grid[3] == [-1] and
            len(game_controller.to_draw.contents) == 1 and
            game_controller.can_drop and
            game_controller.is_dropping)


def test_dropping():
    game_controller = Game_Controller()
    game_controller.dropping()
    assert (not game_controller.is_dropping)

    game_controller = Game_Controller()
    x = game_controller.COL_X_LIST[3]
    y = constant.TOP_SPACE_Y // 2
    game_controller.to_draw.push(Circle(x, y,
                                        game_controller.turn))
    game_controller.dropping()
    assert (game_controller.to_draw.contents[-1].y == y + 20)

    game_controller = Game_Controller()
    x = game_controller.COL_X_LIST[1]
    y = game_controller.TARGET_Y_LIST[0]
    game_controller.to_draw.push(Circle(x, y,
                                        game_controller.turn))
    game_controller.dropping()
    assert (not game_controller.can_drop and
            not game_controller.is_dropping and
            game_controller.turn == -1)


def test_havespace():
    game_controller = Game_Controller()
    assert all(game_controller.havespace(i) for i in range(constant.COL))
    game_controller = Game_Controller()
    game_controller.grid = [[1 for _ in range(constant.ROW)]
                            for _col in range(constant.COL)]
    assert all(not game_controller.havespace(i)
               for i in range(constant.COL))


def test_filled_board():
    game_controller = Game_Controller()
    assert (not game_controller.filled_board())
    game_controller = Game_Controller()
    game_controller.grid = [[1 for _ in range(constant.ROW)]
                            for _col in range(constant.COL)]
    assert (game_controller.filled_board())


def test_callingTurns():
    game_controller = Game_Controller()
    game_controller.callingTurns()
    assert (game_controller.message.string == "Player's turn" and
            game_controller.message.color == "RED")
    game_controller = Game_Controller()
    game_controller.turn = -1
    game_controller.callingTurns()
    assert (game_controller.message.string == "Computer's turn" and
            game_controller.message.color == "YELLOW")


def test_is_winning():
    game_controller = Game_Controller()
    game_controller.grid = [[1, 1, 1, 1], [], [], [], [], [], []]
    assert (game_controller.is_winning(col_i=0, row_j=3, color=1))
    game_controller = Game_Controller()
    game_controller.grid = [[1, 1, 1], [-1], [-1], [-1], [-1], [], []]
    assert (game_controller.is_winning(col_i=4, row_j=0, color=-1))
    game_controller = Game_Controller()
    game_controller.grid = [[1], [-1, 1], [-1, 1, 1],
                            [-1, -1, 1, 1], [1], [], []]
    assert (game_controller.is_winning(col_i=3, row_j=3, color=1))
    game_controller = Game_Controller()
    game_controller.grid = [[1, 1, 1, -1], [-1, 1], [-1], [1], [1], [], []]
    assert (not game_controller.is_winning(col_i=0, row_j=3, color=-1))
