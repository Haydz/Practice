birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}


while True:
    name = raw_input("\nEnter a name:  (blank to quit) ")
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + "is the birthday for " + name)

    else:
        print('I do not have birthday information for ' + name)
        print('what is their birthday')
        bday = raw_input('Enter birthday ')
        birthdays[name] = bday
        print('Birthday database updated')


"""
Cool program acts like a stateless database:
Can either get someones birthday
or enter in someones birthday if its not in the database.

could write to a file and use as a dictionary type weird datbase.

read and writetoo file!

"""






