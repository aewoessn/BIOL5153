#! /bin/bash

# Homework 4
## This code assumes that you are using my file system

## Question 1

# Change to a directory
cd ~/Desktop/watermelon_files/watermelon_nt/

# Create a database
makeblastdb -in nad4L.fasta -dbtype nucl

# Blast for nad4L gene
blastn -query nad4L.fasta -db nad4L.fasta

## Question 2

# Change to a directory
cd ~/Desktop/watermelon_files/watermelon_nt

# Create a database
cat *.fasta | makeblastdb -dbtype nucl -out nt -title nt

# Blast for nad4L gene
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db nt

## Question 3

# Change to a directory
cd ~/Desktop/watermelon_files/

# Create a database
makeblastdb -in watermelon.fsa -dbtype nucl -out watermelon -title watermelon

# Blast for nad4L gene
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db watermelon

## Question 4

# Change to a directory
cd ~/Desktop/watermelon_files/mt_genomes

# Create a database
cat *.fasta | makeblastdb -dbtype nucl -out mt -title mt

# Blast for nad4L gene
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db mt

## Question 5

# Blast for nad4L gene against NCBI "nr" database
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -remote -db nr

## Question 6

# Change to a directory
cd ~/Desktop/watermelon_files/

# Blast for nad4L gene
tblastx -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -db watermelon

## Question 7
# The size of the database is independent of both the raw and bit score.
# The E-value however, is influnenced by the size of the database.
# This is because the E-value depends on random chance of hits you can expect, which from a larger database, tends to increase.

## Question 8

cd ~/Desktop/watermelon_files/

# Blast watermelon genome with the watermelon genome with default parameters
blastn -query watermelon.fsa -db watermelon > default.out

# Blast watermelon genome with the watermelon genome with somewhat sensitive parameters
blastn -outfmt 0 -dust yes -word_size 9 -reward 2 -penalty -3 -gapopen 5 -gapextend 2 -query watermelon.fsa -db watermelon > somewhat.out

# Blast watermelon genome with the watermelon genome with sensitive
blastn -reward 5 -penalty -4 -gapopen 8 -gapextend 6 -word_size 7 -query watermelon.fsa -db watermelon > sensitive.out
