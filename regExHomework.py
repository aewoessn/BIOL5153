#! /usr/bin/env python

import re

# Import the story
story ="Katherine went to the concert to see her favorite band, Catheryn and the Cathryn’s. She ran into her friend Kathryn, who introduced Katherine to her friend, Catherine. Together, they enjoyed the concert while texting inaudible snippets to their mutual friends, Kathrin and katharine.";

# Create a regular expresion
match = re.findall('.?ath.*?n',story,re.I);
if match:
    print('Matches found: ' + match);
else:
    print('No matches found');
