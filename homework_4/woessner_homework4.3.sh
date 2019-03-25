#! /bin/bash

## Question 3

# Change to a directory
cd ~/Desktop/watermelon_files/

# Create a database
makeblastdb -in watermelon.fsa -dbtype nucl -out watermelon -title watermelon

# Blast for nad4L gene
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db watermelon
