import pytest
from SeqKit_tools.modules.transcriber import transcriber

#Regular expected case
def test_transcriber_regular_case ():
    dna = "aggagtaagcccttgcaactggaaatacacccattg"
    result = transcriber(dna)
    expected = "AGGAGUAAGCCCUUGCAACUGGAAAUACACCCAUUG"
    assert result == expected

#Empty sequence provided
def test_transcriber_empter_input ():
    dna = ""
    result = transcriber(dna)
    expected =  ""
    assert result == expected

#Passing a non-string as the sequence should raise a TypeError
def test_transcriber_non_string_sequence ():
    with pytest.raises(TypeError):
        transcriber(10)

#Invalid non-DNA bases shoul raise a Value Error
def test_transcriber_non_DNA_bases_in_sequence ():
    dna = "aggagx"
    with pytest.raises(ValueError):
        transcriber(dna)