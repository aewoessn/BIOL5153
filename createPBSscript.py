#! /usr/bin/env python3

# Create a script that can be easily ran from the terminal

import argparse

parser = argparse.ArgumentParser(description='Create a .PBS script');
parser.add_argument('job', help='The name of the job to be ran');
parser.add_argument('queue',help='The name of the queue to use');
parser.add_argument('nodes',type=int,help='The number of cores to use');
parser.add_argument('walltime',type=int,help='Walltime [in hours]');
parser.add_argument('-e','--email',help='The [optional] email address to use');

args = parser.parse_args();

'''
# Sanity check
print('Job name: ' + args.job + '.PBS');
print('Queue name: ' + args.queue);
print('Number of cores: ' + str(args.nodes));
print('Walltime: ' + str(args.walltime) + ' hours');
if args.email:
    print('Email: ' + args.email);
'''
# Parse the inputs to local variables
jobName = args.job;
queueName = args.queue;
nodes = args.nodes;
walltime = args.walltime;

# Generate the test file to write to
file = open(args.job+'.PBS','w');

# Write out the job name
file.write('#PBS -N ' + jobName + '\n');

# Write out the queue
file.write('#PBS -q ' + queueName + '\n');

# Merge STDOUT and STDERR
file.write('#PBS -j oe \n');

# If emails exist, add the needed lines
if args.email:
    file.write('#PBS -m abe \n');
    file.write('#PBS -M ' + args.email + '\n');

# Create a filename for the STDOUT
file.write('#PBS -o ' + jobName +'.$PBS_JOBID' + '\n');

# Specify nodes, cores, and walltime
file.write('#PBS -l nodes=1:ppn=' + str(nodes) + '\n');
file.write('#PBS -l walltime=' + str(walltime) + ':00:00' + '\n');
file.write('\n');

# Change directory
file.write('cd $PBS_O_WORKDIR' + '\n');
file.write('\n');

# Import some modules
file.write('module purge' + '\n');
file.write('module load python/3.6.0-anaconda' + '\n');

# Thank the file for its time
file.close();
