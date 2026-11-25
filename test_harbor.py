from hello import harbor


def test_harbor():
    assert harbor("World") == "Harbor, World!"
