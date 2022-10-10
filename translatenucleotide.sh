#!/bin/bash

# sanity check
printf "Conda env: $CONDA_DEFAULT_ENV\n"
printf "Python version: $(python --version)\n"
printf "Biopython version: $(conda list | egrep biopython | awk '{print $2}')\n"
printf "Emboss version: $(embossversion 2>&1 | tail -n1)\n"
printf "Bash version: ${BASH_VERSION}\n\n"

outlocation=$(mktemp -d /data/files/XXXXXX)
SCRIPTDIR=$(dirname "$(readlink -f "$0")")
transeq -sequence $1 -frame 6 -outseq $outlocation"/proteintranslation" -table $4 2> /dev/null 
python $SCRIPTDIR"/translatenucleotide.py" -i $outlocation"/proteintranslation" -o $2 -s $3
rm -rf $outlocation
