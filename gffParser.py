#! /usr/bin/env python3

# The purpose of this python script is to correctly parse a .gff and .fsa file

import argparse
from Bio import SeqIO

# Declare functions
def getArgs():
    # Parse the inputs
    parser = argparse.ArgumentParser(description='Parses a .gff and .fasta (.fsa) file');
    parser.add_argument('gffFile',help ='Name of .gff file (with extension)');
    parser.add_argument('fsaFile',help='Name of .fsa file (with extension)');
    return(parser.parse_args());
#end

def openGffFile(fileName):
    # Open the gff file
    file = open(fileName);

    return(file)
#end

def loadFsaSequence(fileName):
    # Open the fasta file using SeqIO
    return(SeqIO.read(fileName,'fasta').seq);
#end

def parseGff(gffLine):
    # Parse every line in the gff file
    content = gffLine.rstrip('\n').split('\t');
    sequence = content[0];
    source = content[1];
    feature = content[2];
    start  = content[3];
    end = content[4];
    score = content[5];
    strand = content[6];
    phase = content[7];
    attributes = content[8];

    return(sequence,source,feature,start,end,score,strand,phase,attributes);
#end

def findSubsequence(fsaSequence,start,end):
    # Pull out the subsequence
    return(fsaSequence[int(start):int(end)]);
#end

def getReverseComplement(sequence):
    # Get the reverse complement
    return(sequence.reverse_complement());
#end

def getGCContent(subSequence):
    # Calculate the G/C content
    return((subSequence.upper().count('G') + subSequence.upper().count('C'))/len(subSequence));
#end

def closeFile(file):
    file.close();
#end

def main():
    # Get arguments
    args = getArgs();

    # Open files
    gffFile = openGffFile(args.gffFile);
    fsaSequence = loadFsaSequence(args.fsaFile);

    reverseComplement = getReverseComplement(fsaSequence);
    # Go through every line in the gff file
    for line in gffFile:
        # Parse the line
        [sequence,source,feature,start,end,score,strand,phase,attributes] = parseGff(line);

        # Check to see if the strand is negative
        if strand == '-':
            print(findSubsequence(reverseComplement,start,end));

        # Get the subsequence
        subSequence = findSubsequence(fsaSequence,start,end);

        # Calculate the G/C content
        gcContent = getGCContent(subSequence);

        print(gcContent)

    closeFile(gffFile);
#end

if __name__ == "__main__":
    main();
