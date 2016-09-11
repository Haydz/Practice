picnicItems = {'Apples' : 5, 'cups' : 2}
print 'I am bringing ' + str(picnicItems.get('cups',0)) + ' cups'
print ' I am bringing ' + str(picnicItems.get('fake', 0)) + ' fake'
"""

Using get method prevents an error message:


>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
File "<pyshell#34>", line 1, in <module>
'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
KeyError: 'eggs'

"""