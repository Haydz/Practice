import re


"""
MATCH NONE OR MORE - different to PLUS
using star, any number of wow will match


to match a literal star \*

"""
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print mo1.group()

mo2 = batRegex.search(r'The Adventures of Batwoman')
print mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowoman')
print mo3.group()