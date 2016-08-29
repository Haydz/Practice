import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search(('My Number is 415-555-4242'))
print ('Group 1 ' + mo.group(1))
print('group 2' + mo.group(2))

#mo for match objects
print('all of it' + mo.group())
print'All groupS:  ' , mo.groups()# calls search on phoneNumRegex

print(' can assign names')
areaCode, mainNumber = mo.groups()
print areaCode, '-> AreaCode'


print 'Escaping characters'
phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My Number is (415) 555-4242')
print mo2.group(1)
print mo2.group(2)