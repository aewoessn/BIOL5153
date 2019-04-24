#! /usr/bin/env python3

import argparse
from collections import defaultdict
import csv

def get_args():
    # Create a parser variable
    parser = argparse.ArgumentParser(description='Removes false frequency-code pairs');

    # Add arguments to the parser
    parser.add_argument('tags_file',help = 'List of real telemetry frequencies and codes');
    parser.add_argument('data_file',help = 'Telemetry data');

    # Return the parsed arguments
    return(parser.parse_args());
#end

def parseTags(tagsFile):
    # Create a dictionary where the keys are the frequencies, and the values are the codes
    codes = defaultdict(dict);

    # Open and read the file (tab delimited)
    with open(tagsFile,'r') as tags:
        dat = csv.reader(tags,delimiter='\t');

        # Skip header line
        next(dat);

        # Go through each line of the file
        for line in dat:
            if not line:
                # Skip blank lines
                continue;
            else:
                # Codes[line[0]] is a **list**, for which we are appending

                # Check to see if this particular key exists
                if line[0] not in codes:
                    codes[line[0]] = [];

                codes[line[0]].append(line[1]);

        # Sanity check
        #for freq,code in codes.items():
        #    print(freq,code);

    return(codes);
#end

def parseData(dataFile,codes):

    with open(dataFile,'r') as data:
        next(data);

        for line in data:
            # Split up at just white-space
            row = line.split();

            # Check to see if frequency is associated with the code
            if row[5] in codes[row[4]]:
                print(line);

#end

def main():
    # Get the parsed arguments
    args = get_args();

    codes = parseTags(args.tags_file);

    parseData(args.data_file,codes);
#end

if __name__ == '__main__':
    main();
