from hello import cheer


def test_cheer():
    assert cheer("World") == "Cheer, World!"
