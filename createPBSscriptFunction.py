#! /usr/bin/env python3

# Create a function that takes in the job name, queue, ppn, and walltime

def createPBSscript(jobName,queue,email,ppn,walltime):
    # Write a text file (PBS script)

    # Create the file in the current directory
    file = open(('%s.PBS') %jobName,'w');

    # Write the job name
    file.write('#PBS -N ' + str(jobName));

    # Select a queue
    file.write('#PBS -q ' + str(queue) + '\n');

    # Merge STDOUT and STDERR
    file.write('#PBS -j oe' + '\n');

    # Send emails
    file.write('#PBS -m abe' + '\n');

    # Specify email
    file.write('#PBS -M ' + str(email) + '\n');

    # Filename for STDOUT
    file.write('#PBS -o ' + str(jobName) +'.$PBS_JOBID' + '\n');

    # Specify nodes, cores, and walltime
    file.write('#PBS -l nodes=1:ppn=' + str(ppn) + '\n');
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
