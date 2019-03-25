#! /bin/bash

## Question 1

# Change to a directory
cd ~/Desktop/watermelon_files/watermelon_nt/

# Create a database
makeblastdb -in nad4L.fasta -dbtype nucl

# Blast for nad4L gene
blastn -query nad4L.fasta -db nad4L.fasta
