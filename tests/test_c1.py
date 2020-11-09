from t1 import Stack
from pytest import fixture, mark


@fixture
def stack():
    return Stack()


@mark.smoke
def test_length(stack):
    assert len(stack) == 0


@mark.smoke
def test_push(stack):
    stack.empty()
    stack.push(1)
    assert len(stack) == 1
    assert stack._stack[-1] == 1


@mark.smoke
def test_pop(stack):
    stack.empty()
    stack.push(10)
    assert len(stack) == 1
    element = stack.pop()
    assert element == 10
    element = stack.pop()
    assert element is None
