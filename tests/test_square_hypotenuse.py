import pytest
from SeqKit_tools.modules.square_hypotenuse import square_hypotenuse

#Regular expected result
def test_square_hypotenuse_regular_case ():
    assert square_hypotenuse(10, 12) == 244

#Passing non-integers should raise a TypeError
def test_square_hypotenuse_non_integer  ():
    with pytest.raises(TypeError):
        square_hypotenuse("a", "b")

#Passing negative integers or 0 should raise a ValueError
def test_square_hypotenuse_negative_integers ():
    with pytest.raises(ValueError):
        square_hypotenuse(0, 12)