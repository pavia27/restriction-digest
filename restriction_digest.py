import argparse
from Bio import SeqIO
import csv
import re

def digest(seq, cut_site, cut_position):
    res_site = [match.start() for match in re.finditer(cut_site, seq)]
    if not res_site:
        return [seq]
    
    cut_seqs = []
    start = 0
    for base in res_site:
        cut_seqs.append(seq[start:base + cut_position])
        start = base + cut_position - len(cut_site) + 1
    cut_seqs.append(seq[start:])
    
    return cut_seqs

def main(args):
    cut_site, cut_position_marker = args.res_site.split("/")
    cut_position = len(cut_site)
    
    with open(args.out, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["header", "number_of_bands", "length_of_bands"])

        for a in SeqIO.parse(args.input, "fasta"):
            cut_seqs = digest(str(a.seq), cut_site + cut_position_marker, cut_position)
            num_band = len(cut_seqs)
            band_lengths = "/".join([str(len(seq)) for seq in cut_seqs])
            csv_writer.writerow([a.id, num_band, band_lengths])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform an in silico restriction digest on many sequences at once")
    parser.add_argument("-in", "--input", required=True, help="file of sequences in fasta format")
    parser.add_argument("-out", "--out", required=True, help="Name of the output file")
    parser.add_argument("--res_site", required=True, help="Restriction site and cut position, e.g., GCG/C, use the / to signify the cut")
    args = parser.parse_args()
    main(args)
