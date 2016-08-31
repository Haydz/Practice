import re

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print mo1.group()

mo2 = batRegex.search('The Adventures of Batwowoman')
print mo2.group()


mo3 = batRegex.search('The Batman')

try:
    print mo3.group()
except:
    print(" sorry no match")

    """

a + will only match on 1 and MORE
different ot the STAR on ZERO or more

    """