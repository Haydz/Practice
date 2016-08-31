import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9997 work: 123-123-0000')
print mo.group()
"""
above prints first match

below prints all matches
"""

mo1 = phoneNumRegex.findall('Cell: 415-555-9997 work: 123-123-0000')
print mo1
"""
Does not use group syntax
No groups means it does not return a match object, but a list of strings.
"""


"""

with groups
returns tuples
"""

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNumRegex2.findall('Cell: 415-555-9997 work: 123-123-0000')
print mo2