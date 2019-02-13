#! /bin/bash

## assn01-1
# Look for files with 'nad' in the file name ion the home directory
find *nad*.*

## assn01-2
# The command to access all of the active processes is "top"
# This particular process is using >1% of my CPU
# From 'top' command:
# KiB Mem : 16305280 total, 13627800 free,  1418552 used
# I got these values from the "header" section that is displayed when calling top
# Text can be copied using Shift+Ctrl+C
top

## assn01-3
# This assumes that you are in the correct directory that contains "watermelon.gff"
grep 'misc_feature' ~/Desktop/watermelon_files/watermelon.gff | column -t | sort -k7nr > IR_regions.gff

## assn01-4
# Find the number features that contain "misc_feature" using word count
grep 'misc_feature' ~/Desktop/watermelon_files/watermelon.gff | column -t | wc -l

# Find the number of features that do not contain "misc_feature" using word count
grep -v 'misc_feature' ~/Desktop/watermelon_files/watermelon.gff | column -t | wc -l

# There are more sequences outside of the IR region

## assn01-5
# The sequence that corresponds to BamHI: GGATCC
# The sequence that corresponds to EcoRI: AATTC
grep -vhB1 "AATTC" ~/Desktop/watermelon_files/watermelon_nt/*.* | grep -B1 "GGATCC"

## assn01-6
# In order to do this, we can grab the first 1000 lines, and then cut off the first 500 lines
head -n1000 ~/Desktop/example_files/shaver_etal.csv | tail -n500

## assn01-7
sort -k2r,2 -k3,3 ~/Desktop/example_files/fruit.txt

