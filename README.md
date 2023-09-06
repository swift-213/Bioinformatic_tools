# Bioinformatic_tools
A collection of scripts that can be used for bioinformatic analysis. All written using python3

## Cloning the repository and downloading requirements
```
git clone https://github.com/swift-213/Bioinformatic_tools.git

cd Bioinformatic_tools

python3 -m pip install -r Bioinformatic_tools_requirements.txt
```
## Subset_fasta.py
This script reads in a fasta file and then pulls out the sequences of variants you have specified in a seperate input list. 
The input list can be in the form of a text file or an excel file. If you are inputting the variants in an excel file you need to specifiy the column name with the `--column_name` flag.

### Command line:
```
python3 Fasta_Parser.py -fa -input -output -xlsx -txt -col_name -fa_parse -suffix
```
### Flags:
| Flag | Long Flag | Description | Required |
|-|-|-|-|
| fa | full_fasta_file | fasta file containing total sequences | True |
| input | input_list | list of variant names to be pulled out | True |
| output | output_location | file name of output file | True |
| xlsx | excel_input | flag required if your input is in excel format | False |
| txt | text_file_input | flag required if your input is in text format | False |
| col_name | column_name | if excel input is used you must give the column a name and use this flag following the column name in ' ' | False |
|fa_parse| Fasta_parse_variant_name | if the name of the variant needs parsed from the longer fasta format. e.g. ENA\|NAME\|LONGER_NAME. The script assumes your variant name will match the NAME part | False |
| suffix | add_suffix | if the fasta variant name has a suffix e.g. .1 that your gene list does not it can be added with this flag follwed by the suffix in '' | False |

Whilst the file formatting flags aren't required you must have one or the script will error out. If using excel **you must include the column name**. 

