#! /usr/bin/env python3

from Bio import SeqIO

genome = SeqIO.read('watermelon.fsa','fasta');

#print(dir(genome)) # List all of the methods available
#print(genome.description);

#print(str(len(genome.seq)))
print(genome.reverse_complement().seq)
