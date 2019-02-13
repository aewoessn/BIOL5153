# Alan Woessner Homework 2

#! /bin/bash

## assn02-1

# Loop through each value between 808 and 8008, and echo TR- with each value
for i in $(seq 808 8008) #this can also be done using {808..8008}
	do
		echo TR-$i
	done

## assn02-2

# Make sure we are in the correct directory
cd ~/Desktop/watermelon_files/watermelon_nt

# Do everything that "bash_loop3.sh" does, with slight modifications
echo '#! /bin/bash'

for file in *nad*.fasta
do

        # print out the perl script I want to run on the current file in my loop
        echo my_python_script.py $file '>' ${file%.fasta}.out

done 

## assn02-3

# Create new alias "la", which both clears the terminal and runs the command ls -al
alias la='clear; ls -al'

# Make sure we are in the correct directory (this will probably always be different,
#  and really only applies to me)
cd ~/Desktop/homework/homework_2/gene_trees

## assn02-4
# Use ls to get files with '.fasta' extension, then pipe into word count for number of lines
ls *.fasta | wc -l

## assn02-5
# Do the same thing to '.tre' and '.sched' extensions
ls *.tre | wc -l

## assn02-6
ls *.sched | wc -l

## assn02-7
# Use the function find to determine if a file exists or not. If it does not, then echo the name,
# and use wc to find out how many there are

for i in *.fasta
	do 
		test -e ${i%.fasta}_raxml.tre || echo ${i} 
done |  wc -l

## assn02-8
# Search through each file for the first match of "Program Return Code:",
# then find the number of lines that have "...: 0" and the ones that do not

grep -m1 'Program Return Code:' *.sched | grep 'Program Return Code: 0' | wc -l

grep -m1 'Program Return Code:' *.sched | grep -v 'Program Return Code: 0' | wc -l

## assn02-9
# See if a file exists, and if it does not, then output the line of code needed
for i in *.fasta
        do 
		 test -e ${i%.fasta}_raxml.tre || echo write_raxml_job_script.py $i '>' ${i%.fasta}.pbs
done 

