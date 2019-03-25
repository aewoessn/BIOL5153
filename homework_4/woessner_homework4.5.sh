#! /bin/bash

## Question 5

# Blast for nad4L gene against NCBI "nr" database
blastn -query ~/Desktop/watermelon_files/watermelon_nt/nad4L.fasta -remote -db nr
