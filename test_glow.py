from hello import glow


def test_glow():
    assert glow("World") == "Glow, World!"
