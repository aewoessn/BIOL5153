#!/usr/bin/env python
# coding: utf-8

# # Programming for Biologists
# ## Chapter 2 In-Chapter Examples 

# ### Using the print function

# In[2]:


# Print out hello world
print("Hello World");

# Try it with using single and double quotes
print('Hello world with single quotes');
print("Hello world with double quotes");

# Add quotations within a print function
print("She said, 'Hello world'");
print('He said, "Hello world"');


# ### Storing strings as variables

# In[3]:


# Create string variable
my_dna = "ATGCGTA";

# Print the data contained within the "my_dna" variable
print(my_dna);

# Make a new variable to show that variable names are arbitrary
banana = "ATGCGTA";

print(banana);


# ### Manipulating strings

# In[1]:


# Add two strings to concatenate them
my_dna = "AATT" + "GGCC";
print(my_dna);

# Concanenate two strings using variables
upstream = "AAA";
downstream = "GGG"
my_dna = upstream + "ATGC" + downstream;

#Concatenate within a print function
print("Hello" + " " + "world");

# Find the length of strings using the function "len"
dna_length = len("ATGC");
print(dna_length);

# In order to print the length, we must convert the output variable to a string
dna_length = len(my_dna);
print("The length of the DNA sequence is " + str(dna_length));

# Change everything to lower case using the "lower" method
print("Before: " + my_dna);
print("After: " + my_dna.lower());

# Replace parts of a string using the "replace" method

## Create a protein string variable
protein = "vlspadktnv";

# Replace v with y
print("Before: " + protein);
print("After: " + protein.replace("v","y"));

# Replace vls with ymt
print("Before: " + protein)
print("After: " + protein.replace("vls","ymt"));

# Extract part of a string

# Pull out characters in positions 3 to 5
print(protein[3:5]);

# Pull out characters in positions 0 to 5
print(protein[0:6]);


# ### Counting and finding substrings

# In[21]:


print(protein);

# Count the amino acid residues
valineCount = protein.count('v');
lspCount = protein.count('lsp');
tryptophanCount = protein.count('w');

# Print the counts
print('valines: ' + str(valineCount));
print('lsp: ' + str(lspCount));
print('tryptophans: ' + str(tryptophanCount));

# Find strings
print(str(protein.find('p')));
print(str(protein.find('kt')));
print(str(protein.find('w')));

