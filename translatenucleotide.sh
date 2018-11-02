#!/bin/bash
transeq -sequence $1 -frame 6 -outseq proteintranslation -table $4 2> /dev/null 
translatenucleotide.py -i proteintranslation -o $2 -s $3
