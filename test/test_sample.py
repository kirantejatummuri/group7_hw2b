def addition(x,y):
    return x + y

def substraction(x,y):
    return x - y

def multiplication(x,y):
    return x*y

def test_addition():
    assert addition(1,1) == 2

def test_substraction():
    assert substraction(10,1) == 9

def test_multiplication():
    assert multiplication(2,3) == 6