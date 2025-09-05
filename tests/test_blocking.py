import pytest
from SeqKit_tools.modules.blocking import blocking

#Regular expected result
def test_blocking_regular_case():                                     
    seq = "aggagtaagcccttgcaactggaaatacacccattg"
    result = blocking(seq, 3) 
    expected = "AGG AGT AAG CCC TTG CAA CTG GAA ATA CAC CCA TTG"
    assert result == expected

#Empty sequence provided
def test_blocking_empty_input():
    seq = ""
    result = blocking(seq,3)
    expected = ""
    assert result == expected

#Blocksize is larger than sequence
def test_blocking_blocksize_larger_than_sequence():
    seq = "aggagt"
    assert blocking(seq, 10) == "AGGAGT"

#Passing a non-string as the sequence should raise a TypeError
def test_blocking_non_string_sequence():                              
    with pytest.raises(TypeError):
        blocking(5, 3)

#Passing a non-integer, 0 or negatvive number as the blocksize should raise a ValueError
def test_blocking_non_integer_blocksize ():                            
    seq = "aggagtaagcccttgcaactggaaatacacccattg"
    with pytest.raises (ValueError):
        blocking(seq, 0)


#Invalid non-DNA bases in the sequence should raise a ValueError
def test_block_non_DNA_bases_in_sequence ():
    seq = "aggagx"
    with pytest.raises(ValueError):
        blocking(seq,10)
    







