#! /bin/bash

## Question 4

# Change to a directory
cd ~/Desktop/watermelon_files/mt_genomes

# Create a database
cat *.fasta | makeblastdb -dbtype nucl -out mt -title mt

# Blast for nad4L gene
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db mt
