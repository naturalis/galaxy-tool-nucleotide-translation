#!/bin/bash

#location for production server
#outlocation=$(mktemp -d /media/GalaxyData/database/files/XXXXXX)
#location for the testserver
#outlocation=$(mktemp -d /media/GalaxyData/files/XXXXXX)
outlocation=$(mktemp -d /home/galaxy/ExtraRef/XXXXXX)
transeq -sequence $1 -frame 6 -outseq $outlocation"/proteintranslation" -table $4 2> /dev/null 
translatenucleotide.py -i $outlocation"/proteintranslation" -o $2 -s $3
rm -rf $outlocation
