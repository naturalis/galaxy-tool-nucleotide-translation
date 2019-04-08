#!/bin/bash
echo "Test text" 
outlocation=$(mktemp -d /home/galaxy/galaxy/database/XXXXXX)
SCRIPTDIR=$(dirname "$(readlink -f "$0")")
transeq -sequence $1 -frame 6 -outseq $outlocation"/proteintranslation" -table $4 2> /dev/null 
python $SCRIPTDIR"/translatenucleotide.py" -i $outlocation"/proteintranslation" -o $2 -s $3
rm -rf $outlocation
