#! /usr/bin/env python

import re

# Example 1
crush = 'Alicia\tKeys';
print(crush);

match = re.search('licia',crush);

if match:
    print('Match found: ' + match.group(0));

# Example 2
match = re.search(r"(a\t)",crush);

if match:
    print('Match found: ' + match.group(1));
else:
    print('No match found');

# Example 3
crush = 'Alicia Keys';
match = re.search('Alicia ([a-zA-Z])',crush);

if match:
    print('Full match: ' + match.group(0));
    print('Captured: ' + match.group(1));
else:
    print('No match');

# Example 4
crush = 'Allllllllllllllllllllicia Keys';
match = re.search('A(l+)icia Keys',crush);
if match:
    print('Full match: ' + match.group(0));
    print('There are ' + str(len(match.group(1))) + " l's in " + match.group(0));
else:
    print('No match');

# Example 5
crush = 'AliciaAliciaAlicia Keys';
match = re.search('(Alicia)+',crush);
if match:
    print('Full match: ' + match.group(0));
    print('Captured: ' + match.group(1));
else:
    print('No match');

# Example 6
crush = 'AliciaKeys';
match = re.search('Alicia(.*)Keys',crush);
if match:
    print('Full match: ' + match.group(0));
    print('Captured: ' + match.group(1));
else:
    print('No match');

# Example 7
crush = 'Beyonce';
match = re.search("(Alicia Keys)*",crush);
if match:
    print('Full match: ' + match.group(0));
    print('Captured: ' + str(match.group(1)));
else:
    print('No match');

# Example 8
crush = 'Beyonce';
match = re.search('Alicia|Beyonce',crush);
if match:
    print('Full match: ' + match.group(0));
else:
    print('No match');

# Example 9
crush = 'Beabcdyonce';
match = re.search("(Be).*(y(on)ce)",crush); # Paraenthesis = groups
if match:
    print('Capture 1: ',match.group(1));
    print('Capture 2: ',match.group(2));
    print('Capture 3: ',match.group(3));
else:
    print('No match');

# Example 10
crush = 'AliciaAliciaAlicia\t\t\tKeys';
match = re.search('((Alicia){2,})(\s+)Keys',crush);
if match:
    print('The third group: [' + match.group(3) + ']');
else:
    print('No match');

# Example 11
crush = 'Alicia Keys';
match = re.search('alicia',crush,re.I); # Case-insensitive
if match:
    print('Found match: ' + match.group());
else:
    print('No match');

# Example 12
cat1 = 'Peaches';
fact = 'We love ' + cat1;

pat = re.compile(cat1);
match = pat.search(fact,re.I);
if match:
    print(match.group(0));

# Example 13
crush = "<BOLD>Holy moly</BOLD>, it's <BOLD>Alicia Keys</BOLD>";

# Example 14
names = 'Katherine, Catheryn, Cathryn, katharine, Katherine, Catherine, Kathrin, Kathryn';
match = re.findall('.?ath.*?n',names,re.I);
