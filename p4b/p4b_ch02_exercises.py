#!/usr/bin/env python
# coding: utf-8

# # Programming for Biologists
# ## Chapter 2 Exercises

# ### Exercise 1
# #### _Calculating the AT content_

# In[30]:


# Initialize the DNA sequence
dnaSeq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT';

# Find the number of occurences of "AT"
occurencesA = dnaSeq.count('A');
occurencesT = dnaSeq.count('T');

# Find how many possible times "AT" can occur
totalNum = len(dnaSeq);

# Calculate the AT content
content = ((occurencesA+occurencesT)/totalNum)*100;

print('The AT content of the dna sequence is: ' + str(content) + '%');


# ### Exercise 2
# #### _Complementing DNA_

# In[31]:


# Initialize the DNA sequence
dnaSeq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT';

# Convert dna sequence to lowercase complements
dnaSeqA = dnaSeq.replace('A','t');
dnaSeqAT = dnaSeqA.replace('T','a');
dnaSeqATC = dnaSeqAT.replace('C','g');
dnaSeqATCG = dnaSeqATC.replace('G','c');

# Print the final sequence
print('Original: ' + dnaSeq.upper());
print('Final: ' + dnaSeqATCG.upper());


# ### Exercise 3
# #### _Restriction fragment lengths_

# In[32]:


# Initialize the DNA sequence
dnaSeq = 'ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT';

# Find where the cut location is
ind = dnaSeq.find('GAATTC');

# Since the cut location is the seoncd location of the motif, add 1 to the ind
ind = ind + 1;

# Calculate the length of each piece after the cut
before = len(dnaSeq[0:ind]);
after = len(dnaSeq[ind:len(dnaSeq)]);

print('Before cut length: ' + str(before));
print('After cut length: ' + str(after));


# ### Exercise 4
# #### _Splicing out introns, part 1_

# In[33]:


# Initialize DNA sequence
dnaSeq = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT';

# Parse the sequence
exon1 = dnaSeq[0:63];
exon2 = dnaSeq[91:len(dnaSeq)];
intron = dnaSeq[64:90];

# Print out the introns and exons
print('First exon: ' + exon1);
print('Second exon: ' + exon2);
print('Intron: ' + intron);


# ### Exercise 5
# #### _Splicing out introns, part 2_

# In[34]:


# Find the total percentage of DNA sequence just for coding
print('Percentage of ' + str(((len(exon1)+len(exon2))/len(dnaSeq))*100))


# ### Exercise 6
# #### _Splicing out introns, part 3_

# In[35]:


# Print the exons in uppercase and introns in lowercase
print(exon1.upper() + intron.lower() + exon2.upper());

