import pytest
@pytest.fixture(autouse=True,scope="session")
def setup_and_teardown():
    print("Open the browser")
    print("Open the test application")
    yield
    print("Close the test application")
    print("Close the browser")