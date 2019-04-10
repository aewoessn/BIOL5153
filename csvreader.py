#! /usr/bin/env python3

# Import required package(s)
import csv

tabOut = 'shaver_etal.tsv';

# Open the data file
with open('shaver_etal.csv','r') as shaver:
    with open(tabOut,'w') as output:
        # Create a csv reader object
        csvDat = csv.reader(shaver,delimiter=',');

        for line in csvDat:
            if not line or line[0] == '':
                continue;
            else:
                # Create a writer object
                lineWriter = csv.writer(output,delimiter='\t',quotechar='"');
                lineWriter.writerow(line);
