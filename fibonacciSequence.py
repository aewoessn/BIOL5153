#! /usr/bin/env python3

import argparse

# Declare function(s)
def get_args():
    parser = argparse.ArgumentParser(description='Return a number from the Fibonacci sequence');
    parser.add_argument('num',type = int,help='The position of the fibonacci sequence to return');

    # Create output group
    group = parser.add_mutually_exclusive_group();
    group.add_argument('-v','--verbose',action='store_true',help='Simple [default] output, containing: [input,fib number]');
    group.add_argument('-s','--simple',action='store_true',help='Verbose output, just returns fib number');

    return(parser.parse_args());

def calcFib(num):
    # Calculate the Fibonacci number
    a,b = 0,1;

    for i in range(num):
        a,b = b, a+b;

    return(a);

def printOutput(verbosity,num,a):
    # Print the output
    if verbosity:
        # Verbose output
        print('Result: '+str(a));
    else:
        # Simple output
        print(num,a);

# Main body of script
def main():
    args = get_args();

    a = calcFib(args.num);

    printOutput(args.verbose,args.num,a);

if __name__ == "__main__":
    main();
