import re

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print mo1.group()

"""
Greedy to start with:
Regex will choose the most matches

"""

haRegex = re.compile(r'(Ha){3,5}')
mo2 = haRegex.search('HaHaHaHaHa')
print mo2.group()

"""
Non Greed is defined by the?
"""

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo3 =  haRegex.search('HaHaHa  lol what HaHaHaHaHa')
print mo3.group()
