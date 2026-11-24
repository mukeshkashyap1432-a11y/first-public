from hello import salute


def test_salute():
    assert salute("World") == "Salute, World!"
