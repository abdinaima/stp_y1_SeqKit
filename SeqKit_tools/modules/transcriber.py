#Import logger
from SeqKit_tools.logger import logger

"""This module is called 'transcriber'.
The function takes 1 argument, a DNA sequence 'dna', and transcribes it by replacing the t (or T) with u (or U).
It returns an RNA sequence 'rna', which can then be used later (e.g. in a later function)"""


def transcriber (dna):

    logger.info(f"Transcribing the DNA sequence '{dna}'")

    try:

        if not isinstance(dna, str):
            raise TypeError ("The sequence must be a string!")
        

        dna = dna.upper()
        logger.debug(f"Sequence converted to uppercase: '{dna}'")

        allowed_bases = {"A", "T", "C", "G"}

        for x in dna:
            if x not in allowed_bases:
                raise ValueError ("Invalid non-DNA bases appear in this sequence!")


        return dna.translate(str.maketrans("T", "U"))
    
    except (TypeError, ValueError) as e:
        logger.error(f"Transcriber failed: {e}")
        raise


if __name__ == "__main__":
    
    dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"

    rna = transcriber(dna)
    
    print(rna)