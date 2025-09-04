
"""This module is called 'transcriber'.
The function takes 1 argument, a DNA sequence 'dna', and transcribes it by replacing the t (or T) with u (or U).
It returns an RNA sequence 'rna', which can then be used later (e.g. in a later function)"""


def transcriber (dna):

    dna = dna.upper()

    allowed_bases = {"A", "T", "C", "G"}

    if not isinstance(dna, str):
        raise TypeError ("The sequence must be a string!")
    
    for x in dna:
        if x not in allowed_bases:
            raise ValueError ("Invalid non-DNA bases appear in this sequence!")

    return dna.translate(str.maketrans("T", "U"))


if __name__ == "__main__":
    
    dna = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    
    rna = transcriber(dna)
    
    print(rna)