import pytest


@pytest.mark.regression
def test_1():
    a = 5
    b = 10
    assert a<b, "If assertion is passed then it will be not displayed"

@pytest.mark.regression
def test_2():
    a = 10
    b = 11
    assert a==b, "If assertion is failed then it will be displayed"

@pytest.mark.sanity
def test_3():
    a = "Rubel"
    b = "Riyon"
    assert a.__eq__(b)

