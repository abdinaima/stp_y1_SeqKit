#Import logger 
from SeqKit_tools.logger import logger

"""This module is called 'two_slices'.
The function takes 4 arguments: a DNA sequence 'seq' and two pairs of integers.
The first pair of integers is defined by 'n1' and 'n2'.
The second pair of integers is defined by 'n3' and 'n4'.
The function returns 2 slices of the DNA sequence, between the positions represented by the two number pairs inclusively"""


def two_slices (seq, n1, n2, n3, n4):

    logger.info(f"Slicing the sequence '{seq}' into 2 slices between positions {n1},{n2} and positions {n3},{n4}")

    try:

        if not isinstance (seq, str):
            raise TypeError ("Sequence must be a string!")

        seq = seq.upper()
        logger.debug(f"Sequence converted to uppercase: {seq}")

        
        allowed_bases = {"A", "T", "C", "G"}

        for x in seq:
            if x not in allowed_bases:
                raise ValueError ("Invalid non-DNA bases appear in this sequence!")


        if not isinstance(n1,int) or not isinstance(n2,int) or not isinstance(n3,int) or not isinstance(n4,int):
            raise TypeError ("All 4 numbers must be integers!")
        
        if n1 <0 or n2<0 or n3<0 or n4<0:
            raise ValueError ("All 4 numbers must be positive!")


        return seq[n1:n2+1] + " " + seq[n3:n4+1]
    
    except (TypeError, ValueError) as e:
        logger.error(f"Two slices failed: {e}")
        raise
    

if __name__ == "__main__":
    
    seq = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    
    n1 = 137
    n2 = 143
    n3 = 274
    n4 = 280

    print(two_slices(seq, n1, n2, n3, n4))


