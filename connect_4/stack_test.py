from stack import Stack


def test_constructor():
    new_stack = Stack()
    assert (new_stack.contents == [])


def test_push():
    new_stack = Stack()
    new_stack.push(1)
    assert (new_stack.contents == [1])
    new_stack.push(2)
    assert (new_stack.contents == [1, 2])


def test_pop():
    new_stack = Stack()
    new_stack.push(1)
    assert (new_stack.pop() == 1 and
            new_stack.contents == [])
    new_stack.push(1)
    new_stack.push(2)
    assert (new_stack.pop() == 2 and
            new_stack.contents == [1])


def test_peek():
    new_stack = Stack()
    new_stack.push(1)
    assert (new_stack.peek() == 1 and
            new_stack.contents == [1])
    new_stack.push(2)
    assert (new_stack.peek() == 2 and
            new_stack.contents == [1, 2])


def test_is_empty():
    new_stack = Stack()
    assert (new_stack.is_empty() is True)
    new_stack = Stack()
    new_stack.push(1)
    assert (new_stack.is_empty() is False)
