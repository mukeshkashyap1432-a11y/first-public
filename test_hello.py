from hello import greet, shout


def test_greet():
    assert greet("World") == "Hello, World!"


def test_shout():
    assert shout("hello") == "HELLO!"
