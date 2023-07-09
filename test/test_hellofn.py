from hellofn import hello


def test_defaul():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David"
