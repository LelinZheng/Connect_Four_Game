from message import Message
from constant import WIDTH, TOP_SPACE_Y


def test_constructor():
    text = "Computer Wins"
    color = "RED"
    message = Message(text, color)
    assert (
            message.x == WIDTH/2
            and message.y == TOP_SPACE_Y/2
            and message.string == "Computer Wins"
            and message.color == "RED"
            )
    text = "Human Wins"
    color = "YELLOW"
    message = Message(text, color)
    assert (
            message.x == WIDTH/2
            and message.y == TOP_SPACE_Y/2
            and message.string == "Human Wins"
            and message.color == "YELLOW"
            )
