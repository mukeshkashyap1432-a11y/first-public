from hello import greet_brief


def test_greet_brief():
    assert greet_brief("World") == "Hi, World."