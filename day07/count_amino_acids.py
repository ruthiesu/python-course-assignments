import sys

codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}

def transpose_codon_table(codon_table):
    transposed = {}
    for amino_acid, codons in codon_table.items():
        for codon in codons:
            transposed[codon] = amino_acid
    return transposed


if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

try:
    with open(filename, "r") as input_file:
        input_text = input_file.read()
except Exception as err:
    print('Could not read file:', filename, err)
    exit(1)

words = input_text.split()

codon_to_amino_acid = transpose_codon_table(codon_table)

my_map = {}

for obj in words:
    if obj in codon_to_amino_acid:
        obj = codon_to_amino_acid[obj]
        if obj in my_map:
            my_map[obj] += 1
        else:
            my_map[obj] = 1

for key, value in my_map.items():
    print(f"{key:<14}  {value:>3}")




