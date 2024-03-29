from Bio import SeqIO
import pandas as pd
from argparse import ArgumentParser
from tqdm import tqdm

parser = ArgumentParser()

parser.add_argument("-fa", "--full_fasta_file", help="fasta file containing total sequences", required=True)
parser.add_argument("-input", "--input_list", help="list of variant names to be pulled out", required=True)
parser.add_argument("-output", "--output_location", help="file name of output file", required=True)
parser.add_argument("-xlsx", "--excel_input", help="flag required if your input is in excel format", required=False)
parser.add_argument("-fa_parse", "--Fasta_parse_variant_name", help="if the name of the variant needs parsed. e.g. ENA|NAME|LONGER_NAME. The script assumes your variant name will match the NAME part.", action='store_true')
parser.add_argument("-not_excel", "--not_excel_file_input", help="flag required if your input is in excel format", required=False)
parser.add_argument("-col_name", "--column_name", help="if excel input is part of a larger table the name of the column that has the variant names", required=False)
parser.add_argument("-suffix", "--add_suffix", help="if the fasta variant name has a suffix e.g. .1 that your gene list does not it can be added with this flag follwed by the suffix in ''", required=False)

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

#loading variable files from an excel file
if args.excel_input == True:
    dataframe1 = pd.read_excel(args.input_list)
    if args.column_name == True:
        positions= dataframe1[args.column_name]

#loading variable names from a text file 
if args.not_excel_file_input == True:
    gene_file_list = (args.input_list)
    positions=[]
    with open(gene_file_list)as f:
        for line in f:
            positions.append(line.strip())

#if your gene list requires a suffix that is present in the fasta file it can be added here.
if args.add_suffix == True:
    append_str1 = '.'
    append_str2 = str(args.add_suffix)

    int_table2=[]
    for sub in positions:
        variable = str(sub)
        int_table2.append(variable + append_str1)
    
    positions=[]
    for sub in int_table2:
        variable = str(sub)
        positions.append(variable + append_str2)


#Parsing the fasta file to be only the variants from the variant list if the variant name needs to be parsed
if args.Fasta_parse_variant_name:
    fasta_dict={}
    for line in tqdm(positions):
        for key, value in seq_dict.items():
            one, two, three = key.split('|')
            if two == line:
                fasta_dict[key] = value
else:
    #Parsing the fasta file to be only the variants from the variant list if the variant name doesn't to be parsed
    fasta_dict={}
    for line in tqdm(positions):
        for key, value in seq_dict.items():
            one, two = key.split(' ', 1)
            #print(one)
            if one == line:
                fasta_dict[key] = value

#Exporting the fasta dictionary as a fasta file
write_fasta(fasta_dict, args.output_location, wrap=80)

#Script statistics
print("The input fasta had", len(seq_dict),"variant sequences.", "You wanted", len(positions),"variant sequences", "You have", len(fasta_dict),"total variant sequenced in your parsed fasta " )
