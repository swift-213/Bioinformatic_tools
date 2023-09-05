from Bio import SeqIO
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm

parser = ArgumentParser()

parser.add_argument("-fa", "--full_fasta_file", help="fasta file containing total sequences", required=True)
parser.add_argument("-input", "--input_list", help="list of variant names to be pulled out", required=True)
parser.add_argument("-output", "--output_location", help="file name of output file", required=True)
parser.add_argument("-xlsx", "--excel_input", help="flag required if your input is in excel format", required=False)
parser.add_argument("-txt", "--text_file_input", help="flag required if your input is in excel format", required=False)
parser.add_argument("-col_name", "--column_name", help="if excel input is part of a larger table the name of the column that has the variant names", required=False)

args = parser.parse_args()

#Definition for formatting and outputting our fasta dictionary as a fasta file
#https://www.programcreek.com/python/?CodeExample=write+fasta 
def write_fasta(seqs, fasta_file, wrap=80):
    """Write sequences to a fasta file.

    Parameters
    ----------
    seqs : dict[seq_id] -> seq
        Sequences indexed by sequence id.
    fasta_file : str
        Path to write the sequences to.
    wrap: int
        Number of AA/NT before the line is wrapped.
    """
    with open(fasta_file, 'w') as f:
        for gid, gseq in seqs.items():
            f.write('>{}\n'.format(gid))
            for i in range(0, len(gseq), wrap):
                f.write('{}\n'.format(gseq[i:i + wrap])) 


seq_dict = {rec.description : rec.seq for rec in SeqIO.parse(args.full_fasta_file, "fasta")}
seq_dict = {rec.description : rec.seq for rec in SeqIO.parse('/Users/frankieswift/Desktop/uniprot-download_true_format_fasta_query__28_28proteome_3AUP00000897-2022.08.26-09.54.41.61.fasta', "fasta")}

#loading variable files from an excel file
if args.excel_input == True:
    dataframe1 = pd.read_excel(args.input_list)
    if args.column_name == True:
        positions= dataframe1[args.column_name]

#loading variable names from  a text file 
if args.text_file_input == True:
    gene_file_list = (args.input_list)
    gene_file_list = ('/Users/frankieswift/Desktop/gene_list.txt')
    positions=[]
    with open(gene_file_list)as f:
        for line in f:
            positions.append(line.strip())

#creating a list of variable names 
gene_names=[]
for row in positions:
    gene_names.append(row)

#Create a fasta dictionary that contains the sequence name that matches the input file 
fasta_dict={}
for key, value in seq_dict.items():
    one, two, three = key.split('|')
    fasta_dict[two] = value

#Subsetting the fasta dictionary so that it contains onlt those sequences that we want to pull out 
new_fasta_dict={}
for line in gene_names:
    for key, value in fasta_dict.items():
        if key == line:
            new_fasta_dict[key] = value

#creating a version of the subsetted fasta will the full descriptive fasta description for export
export_fasta={}
for key in tqdm(seq_dict):
    one, two, three = key.split('|')
    for key1, value1 in new_fasta_dict.items():
        if key1 == two:
            export_fasta[key] = value1

#Exporting the fasta dictionary as a fasta file
write_fasta(export_fasta, args.output_location, wrap=80)

#Script statistics
print("The input fasta had:", len(seq_dict),"variant sequences.", "You wanted", len(gene_names),"variant sequences", "You have", len(export_fasta),"total variant sequenced in your parsed fasta " )
