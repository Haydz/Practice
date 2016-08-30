import re
heroRegex = re.compile(r'Batman|Tina Fey')
#only first instance is returned if BOTH is true
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print mo2.group()

#get all matches
print heroRegex.findall('Tina Fey and Batman.')


#specify prefixes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print mo3.group()
print mo3.group(1)