#!/usr/bin/python
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser(description='')
requiredArguments = parser.add_argument_group('required arguments')
requiredArguments.add_argument('-i', metavar='input fasta', dest='input', type=str,required=True)
requiredArguments.add_argument('-o', metavar='output', dest='output', type=str, required=True)
requiredArguments.add_argument('-s', metavar='output setting', dest='setting', type=str,required=True)
args = parser.parse_args()

def find_stop_codons(writeLine):
    with open(args.output, "a") as output:
        if args.setting == "seqonly":
            output.write("\t".join([writeLine["seqId"],writeLine["1"],writeLine["2"],writeLine["3"],writeLine["4"],writeLine["5"],writeLine["6"]])+"\n")
        elif args.setting == "countonly":
            frame1stopcodons = str(writeLine["1"].count('*'))
            frame2stopcodons = str(writeLine["2"].count('*'))
            frame3stopcodons = str(writeLine["3"].count('*'))
            frame4stopcodons = str(writeLine["4"].count('*'))
            frame5stopcodons = str(writeLine["5"].count('*'))
            frame6stopcodons = str(writeLine["6"].count('*'))
            stopcodonCounts = "\t".join([frame1stopcodons,frame2stopcodons,frame3stopcodons,frame4stopcodons,frame5stopcodons,frame6stopcodons])
            output.write(writeLine["seqId"]+"\t"+stopcodonCounts+"\n")
        elif args.setting == "seqandcount":
            frame1stopcodons = str(writeLine["1"].count('*'))
            frame2stopcodons = str(writeLine["2"].count('*'))
            frame3stopcodons = str(writeLine["3"].count('*'))
            frame4stopcodons = str(writeLine["4"].count('*'))
            frame5stopcodons = str(writeLine["5"].count('*'))
            frame6stopcodons = str(writeLine["6"].count('*'))
            stopcodonCounts = "\t".join([frame1stopcodons,frame2stopcodons,frame3stopcodons,frame4stopcodons,frame5stopcodons,frame6stopcodons])
            sequences = "\t".join([writeLine["1"],writeLine["2"],writeLine["3"],writeLine["4"],writeLine["5"],writeLine["6"]])
            output.write(writeLine["seqId"]+"\t"+stopcodonCounts+"\t"+sequences+"\n")

def translate():
    with open(args.input, "r") as input:
        writeLine = {}
        #sequences = []
        for seq in SeqIO.parse(input, "fasta"):
            sequenceId = "_".join(str(seq.id).split("_")[:-1])
            sequence = str(seq.seq)
            frame = str(seq.id).split("_")[-1]
            writeLine[frame] = sequence
            if frame == "6":
                writeLine["seqId"] = sequenceId
                #sequences.append(writeLine)
                find_stop_codons(writeLine)
                writeLine = {}
    #return sequences

def main():
    translate()

if __name__ == '__main__':
    main()
