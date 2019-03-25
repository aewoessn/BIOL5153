#! /bin/bash

## Question 2

# Change to a directory
cd ~/Desktop/watermelon_files/watermelon_nt

# Create a database
cat *.fasta | makeblastdb -dbtype nucl -out nt -title nt

# Blast for nad4L gene
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db nt
