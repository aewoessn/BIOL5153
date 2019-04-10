#! /usr/bin/env python3

# The purpose of this python script is to correctly parse a .gff and .fsa file

# Add argparse for gff and fasta files

gffFile = open('watermelon.gff');
fsaFile = open('watermelon.fsa');

# Open the gff file

for gffLine in gffFile:

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

    # Pull out the sequences from the fsa file
    for fsaLine in fsaFile:
        if not fsaLine.startswith('>'):
            fsaSequence = fsaLine;

    # Pull out the subsequence
    subSequence = fsaSequence[int(start):int(end)];

    # Calculate the G/C content
    GCcontent = (subSequence.upper().count('G') + subSequence.upper().count('C'))/len(subSequence);
    print(GCcontent)

gffFile.close();
fsaFile.close();
