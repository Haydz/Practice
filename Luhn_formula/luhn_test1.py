#This is a python version of the Luhn algorithm as created in C++ with the think like a hacker programming book



# The Luhn formula is a widely used system for validating identification numbers. Using
# the original number, double the value of every other digit. Then add the values of the
# individual digits together (if a doubled value now has two digits, add the digits indi-
# vidually). The identification number is valid if the sum is divisible by 10.
# Write a program that takes an identification number of arbitrary length and
# determines whether the number is valid under the Luhn formula. The program must
# process each character before reading the next one.


# individually get digits


#double digits -  if greater than 10 the the individual digits get added together.

###This section adds a doubled digit above 10 together

import sys


#now to add every 2nd position


#maybe change string into list?

def DoublingDigit(intdigit):
    intdigit = intdigit * 2
    if intdigit >= 10:
        teststring = str(intdigit)
        # print "test"
        # print intdigit *2
        # print teststring
        Adddigit = 0
        for x in teststring:
            Adddigit += int(x)
        print " added digits =", Adddigit
        return Adddigit
    else:
        print " Doubled Digit digits =", intdigit
        return intdigit


print " enter a  6 digit between 0-9"
digit = raw_input(">")
digit = str(digit)
totaldigit = 0
for position, number in enumerate(digit): #this enumerates the data and adds the file
    print "position: ", position , " Number: ", number
    intdigit = int(number)
    #even
    if position % 2 == 0: #if position is even double it
        totaldigit += DoublingDigit(intdigit)
        print "totaldigit=", totaldigit
        raw_input("PAUSE")


        # intdigit = intdigit *2
        # if intdigit >= 10:
        #     teststring = str(intdigit)
        #     # print "test"
        #     # print intdigit *2
        #     # print teststring
        #     Adddigit = 0
        #     for x in teststring:
        #         Adddigit += int(x)
        #
        #     print "Doubled intdigit: and added together", intdigit, "is: ", Adddigit
        #
        #     totaldigit += Adddigit
        #     print "Adding too total digit: ", totaldigit
        # else:
        #     doubledDigit = intdigit
        #     totaldigit += intdigit
        #     print "Double was not above 10", doubledDigit, " position ", position
    else:
        print" Number was odd position so not doubled, position: ", position
        print "Number was: ", number
        totaldigit += intdigit
        print "totaldigit = ", totaldigit

print "FINAL SUM EQUALS ", totaldigit

if totaldigit % 10 == 0:
    print "CHECKSUM is valid! Checksum is divisiable by 10"

else:
    print "CHECKSUM IS INVALID"






#liststart = []
#for x in
#print digit.split()
# raw_input("PAUSE")
# for x in digit:
#     #print type(digit)
#     print" Printing digit: ", x
#     #raw_input("PAUSE")
#     intdigit = int(x)
#     if (intdigit * 2) > 10:
#         teststring = str(intdigit *2)
#         #print "test"
#         #print intdigit *2
#         #print teststring
#         Adddigit = 0
#         for x in teststring:
#             Adddigit += int(x)
#
#         print "Doubled intdigit:", intdigit, "is: " ,Adddigit




#this section takes in 6 digits and adds digits doubled higher than 10

# print " enter a  6 digit between 0-9"
# digit = raw_input(">")
# digit = str(digit)
#
# for x in digit:
#     #print type(digit)
#     print" Printing digit: ", x
#     #raw_input("PAUSE")
#     intdigit = int(x)
#     if (intdigit * 2) > 10:
#         teststring = str(intdigit *2)
#         #print "test"
#         #print intdigit *2
#         #print teststring
#         Adddigit = 0
#         for x in teststring:
#             Adddigit += int(x)
#
#         print "Doubled intdigit:", intdigit, "is: " ,Adddigit



        #
        # print " enter a digit between 0-9"
        # digit = raw_input(">")
        # intdigit = int(digit)
    # ###This section adds a doubled digit above 10 together
    # if (intdigit * 2) > 10:
    #     teststring = str(intdigit * 2)
    #     print "test"
    #     print intdigit * 2
    #     print teststring
    #     Adddigit = 0
    #     for x in teststring:
    #         Adddigit += int(x)
    #
    #     print Adddigit




