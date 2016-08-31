import re

"""
Regex can use other classes than \d

\w any letter, numeric digit, or underscore chaacter
\s any space tab or new line character "space characters"

"""

xmasRegex = re.compile(r'\d+\s\w+')
mo1 = xmasRegex.findall('12 dummers, 11 pipers, 10 lords, 9 ladies')
print mo1
for x in mo1:
    print x


"""
Make own character classes

"""

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo2 = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print mo2