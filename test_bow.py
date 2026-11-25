from hello import bow


def test_bow():
    assert bow("World") == "Bow, World!"
