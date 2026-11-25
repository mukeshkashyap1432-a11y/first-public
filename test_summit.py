from hello import summit


def test_summit():
    assert summit("World") == "Summit, World!"
