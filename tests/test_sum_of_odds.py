import pytest
from SeqKit_tools.modules.sum_of_odds import sum_of_odds

#Regular expected result
def test_sum_of_odds_regular_case ():
    assert sum_of_odds(10,25) == 144

#Passing non-integers should raise a TypeError
def test_sum_of_odds_non_integer ():
    with pytest.raises(TypeError):
        sum_of_odds("10", 25)

#Passing 0 or a negative integer should raise a ValueError
def test_sum_of_odds_negative_integer ():
    with pytest.raises(ValueError):
        sum_of_odds(-10,25)

#Both integers are the same even number
def test_sum_of_odds_integers_same_even ():
    assert sum_of_odds(10,10) == 0

#Both integers are the same odd number
def test_sum_of_odds_integers_same_odd ():
    assert sum_of_odds(25,25) == 25
  