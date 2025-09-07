import pytest
from SeqKit_tools.modules.two_slices import two_slices

#Regular expected case
def test_two_slices_regular_case():
    seq = "aggagtaagcccttgcaactggaaatacacccattg"
    assert two_slices(seq, 2, 4, 10, 14) == "GAG CCTTG"

#Empty sequence provided
#Function creates a gap between 2 slices, so and empty string would still create a gap
def test_two_slices_empty_input():
    seq = ""
    assert two_slices(seq, 2, 4, 10, 14) == " "  

#Position larger than sequence
def test_two_slices_position_larger_than_sequence():
    seq = "aggagtaagcccttgcaactggaaatacacccattg"
    assert two_slices(seq, 0, 3, 30, 40) == "AGGA CCATTG"

#Passing a non-string as the sequence should raise a TypeError
def test_two_slices_non_string_sequence():
    seq = "aggagtaagcccttgcaactggaaatacacccattg"                              
    with pytest.raises(TypeError):
        two_slices(5, 2, 4, 10, 14 )

#Invalid non-DNA bases in the sequence should raise a ValueError
def test_two_slices_non_DNA_bases_in_sequence ():
    seq = "xaggagtaagcccttgcaactggaaatacacccattg"
    with pytest.raises(ValueError):
        two_slices(seq, 2, 4, 10, 14)

#Passing a non-integer as the positions should raise a TypeError
def test_two_slices_non_integer_position (): 
    seq = "aggagtaagcccttgcaactggaaatacacccattg"
    with pytest.raises (TypeError):
        two_slices(seq, 2, 4, 10, "14")

#Passing negatvive number as the position should raise a ValueError
def test_two_slices_negative_position ():                            
    seq = "aggagtaagcccttgcaactggaaatacacccattg"
    with pytest.raises (ValueError):
        two_slices(seq, -2, 4, 10, 14)

