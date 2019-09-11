import pytest
from calculator import Calculator
#functions must have test_ in front of name
# Arrange
# Act
# Assert
def test_add():
    calculator = Calculator()

    result = calculator.add(2,3)

    assert result == 5

def test_subtract():
    calculator = Calculator()

    result = calculator.subtract(9,3)

    assert result == 6
