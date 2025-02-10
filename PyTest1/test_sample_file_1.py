import pytest


@pytest.mark.sanity
def test_sample_one():
    print("Test message one")

@pytest.mark.sanity
def test_sample_two():
    print("Test message two")

@pytest.mark.smoke
def test_sample_three():
    print("Test message three")