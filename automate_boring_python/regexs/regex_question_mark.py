import re

batRegex = re.compile((r'Bat(wo)?man'))
v('The Adventures of Batman')
print mo1.group()

mo2 = batRegex.search("The Adventures of Batwoman")
print mo2.group()

"""
The ? mark allows a regex to match whether a chosen part of the regex matches or not ()?
The pattern wow is optional
"""

"""
Regex with phone numbers that do or dont have an area code
"""
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo3 = phoneRegex.search('My number is 415-555-4242')
print mo3.group()

mo4 = phoneRegex.search('My number is 555-4242')
print "The same regex works on a number without an area code"
print mo4.group()