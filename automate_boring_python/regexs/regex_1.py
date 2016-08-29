import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(('My Number is 415-555-4242'))
print ('Phone number found: ' + mo.group())

#mo for match objects
# calls search on phoneNumRegex

