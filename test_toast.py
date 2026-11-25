from hello import toast


def test_toast():
    assert toast("World") == "Toast, World!"
