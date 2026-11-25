from hello import hail


def test_hail():
    assert hail("World") == "Hail, World!"
