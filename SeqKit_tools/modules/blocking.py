
"""This module is called 'blocking'.
The function takes 2 arguments, a DNA sequence 'seq' and an integer 'blocksize'.
The function then prints the sequence in blocks of the desired size, with gaps seperating the blocks."""


def blocking (seq, blocksize):

    i = 0
    blocks = []

    if not isinstance(seq, str):
        raise TypeError ("Sequence must be a string!")
    
    if not isinstance(blocksize, int) or blocksize <= 0:
        raise ValueError ("The blocksize must be a positive integer!")

    while i < len(seq):
        blocks.append(seq[i:i+blocksize])
        i +=blocksize
    
    return " ".join(blocks)

if __name__ == "__main__":
    
    seq = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    
    blocksize = 10

    print(blocking(seq, blocksize))