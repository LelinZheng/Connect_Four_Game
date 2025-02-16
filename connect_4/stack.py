class Stack:
    """A simple stack for saving circle placement"""
    def __init__(self):
        self.contents = []

    def push(self, item):
        self.contents.append(item)

    def pop(self):
        if len(self.contents) > 0:
            return self.contents.pop()

    def peek(self):
        if len(self.contents) > 0:
            return self.contents[-1]

    def is_empty(self):
        if len(self.contents) == 0:
            return True
        else:
            return False
