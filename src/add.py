# app.py
# This is a test commit !!!!
def add(a, b):
    return a + b

def test_add():
    assert add(1, 5) == 6
    assert add(2, -2) == 0
    assert add(3, -2) == 1
    assert add(1, -1) == 0
    assert add(7, 2) == 9
