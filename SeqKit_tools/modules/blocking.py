#Import logger 
from SeqKit_tools.logger import logger

"""This module is called 'blocking'.
The function takes 2 arguments, a DNA sequence 'seq' and an integer 'blocksize'.
The function then prints the sequence in blocks of the desired size, with gaps seperating the blocks."""


def blocking (seq, blocksize):

    logger.info(f"Blocking the sequence '{seq}' into blocks of {blocksize}.")

    try:
        seq = seq.upper()
        logger.debug(f"Sequence converted to uppercase: '{seq}'")

        allowed_bases = {"A", "T", "C", "G"}

        if not isinstance(seq, str):
            raise TypeError ("Sequence must be a string!")
        
        for x in seq:
            if x not in allowed_bases:
                raise ValueError ("Invalid non-DNA bases appear in this sequence!")

        if not isinstance(blocksize, int) or blocksize <= 0:
            raise ValueError ("The blocksize must be a positive integer!")
        
        

        i = 0
        blocks = []

        while i < len(seq):
            blocks.append(seq[i:i+blocksize])
            i +=blocksize
        
        logger.debug(f"Generated {len(blocks)} blocks.")
        
        return " ".join(blocks)
    
    except (TypeError, ValueError) as e:
        logger.error (f"Blocking failed: {e}")
        raise



if __name__ == "__main__":
    
    seq = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"

    blocksize = 10

    print(blocking(seq, blocksize))