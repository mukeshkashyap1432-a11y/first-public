from hello import welcome


def test_welcome():
    assert welcome("World") == "Welcome, World!"
