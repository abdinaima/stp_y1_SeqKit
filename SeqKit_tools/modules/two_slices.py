
"""This module is called 'two_slices'.
The function takes 4 arguments: a DNA sequence 'seq' and two pairs of integers.
The first pair of integers is defined by 'n1' and 'n2'.
The second pair of integers is defined by 'n3' and 'n4'.
The function returns 2 slices of the DNA sequence, between the positions represented by the two number pairs inclusively"""


def two_slices (seq, n1, n2, n3, n4):
    
    if not isinstance (seq, str):
        raise TypeError ("Sequence must be a string!")

    if not isinstance(n1,int) or not isinstance(n2,int) or not isinstance(n3,int) or not isinstance(n4,int):
        raise TypeError ("All 4 numbers must be integers!")
    
    if n1 <0 or n2<0 or n3<0 or n4<0:
        raise ValueError ("All 4 numbers must be positive!")

    return seq[n1:n2] + " " + seq[n3:n4]
    

if __name__ == "__main__":
    
    seq = """GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAG
GAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCT
TCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTC
TGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTG
AAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAG
GAGCCTACAAGAAAGTACGAGATTTGAT"""
    
    n1 = 137
    n2 = 143
    n3 = 274
    n4 = 280

    print(two_slices(seq, n1, n2, n3, n4))

