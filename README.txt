Simulate a restriction digest. The user provides a set of DNA sequences in fasta format, the restriction site, and an output file name. 

Requirements:
- python 3.6 or higher
- Biopython installed (pip install biopython)

Output file:
The output is in csv format. 
Header - header of each sequence in the fasta file
number_of_bands - predicted number of fragments produced by the restriction digest
length_of_bands - the lenght of each fragment, separated by /
