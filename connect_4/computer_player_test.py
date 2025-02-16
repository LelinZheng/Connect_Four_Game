from constant import COL_0_X, COL_SPACE, COL, ROW
from computer_player import ComputerPlayer


def test_constructor():
    grid = [[], [], [], [], [], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.grid == [[], [], [], [], [], [], []]
        and computer_player.endgame is False
        and computer_player.COL_X_LIST ==
        [COL_0_X + x * COL_SPACE for x in range(COL)]
    )
    grid = [[1], [1], [1], [1], [], [], []]
    endgame = True
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.grid == [[1], [1], [1], [1], [], [], []]
        and computer_player.endgame is True
        and computer_player.COL_X_LIST ==
        [COL_0_X + x * COL_SPACE for x in range(COL)]
    )


def test_x_to_place():
    grid = [[1, 1, 1], [], [], [], [], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.x_to_place() == computer_player.COL_X_LIST[0]
        )

    grid = [[], [], [-1], [-1], [-1], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.x_to_place() == computer_player.COL_X_LIST[5]
        )

    grid = [[1 for _ in range(ROW)] for _col in range(COL)]
    endgame = True
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.x_to_place() == -1
        )


def test_stop_win():
    grid = [[1], [1], [1], [], [], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.stop_win() == computer_player.COL_X_LIST[3]
        )
    grid = [[], [], [], [1], [1], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.stop_win() == computer_player.COL_X_LIST[5]
        )
    grid = [[1, 1, 1], [], [], [1], [1], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.stop_win() == computer_player.COL_X_LIST[0]
        )


def test_almost_win():
    grid = [[-1, -1, -1], [], [], [], [], [], []]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.almost_win() == computer_player.COL_X_LIST[0]
        )
    grid = [[], [], [], [], [-1], [-1], [-1]]
    endgame = False
    computer_player = ComputerPlayer(grid, endgame)
    assert (
        computer_player.almost_win() == computer_player.COL_X_LIST[3]
        )
