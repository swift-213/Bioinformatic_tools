# Bioinformatic_tools
A collection of scripts that can be used for bioinformatic analysis

## Cloning the repository and downloading requirements
```
git clone https://github.com/swift-213/Bioinformatic_tools.git

cd Bioinformatic_tools

python3 -m pip install -r Bioinformatic_tools_requirements.txt
```
## Fasta_Parser.py
This script reads in a fasta file and then pulls out the sequences of variants you have specified in a seperate input list. 
The input list can be in the form of a text file or an excel file. If you are inputting the variants in an excel file you need to specifiy the column name with the `--column_name` flag.

### Command line:
```
python Fasta_Parser.py -fa -input -output -xlsx -txt -col_name
```
### Flags:
| Flag | Long Flag | Description | Required |
|-|-|-|-|
| -fa | --full_fasta_file | fasta file containing total sequences | True |
| -input | --input_list | list of variant names to be pulled out | True |
| -output | --output_location | file name of output file | True |
| -xlsx | --excel_input | flag required if your input is in excel format | False |
| -txt | --text_file_input | flag required if your input is in excel format | False |
| -col_name | --column_name | if excel input is used you must give the column a name and use this falg following the column name in '' | False |

Whilst the file formatting flags aren't required you must have one or the script will error out. If using excel **you must include the column name**. 

### Fasta format
THe script assumes the formatting of the fasta file is as follows:

\>Depository_code|chrom_name_that_matches_list|longer_chrom_name *description* 


SEQUENCE

The important aspect is that the input variant list needs to match the |1|2|3|, 2nd field in the fasta name or the script will error out. 
