/* A message has been encoded as a text stream that is to be read character by charac-
# ter. The stream contains a series of comma-delimited integers, each a positive number
# capable of being represented by a C++ int . However, the character represented by
# a particular integer depends on the current decoding mode. There are three modes:
# uppercase, lowercase, and punctuation.
# In uppercase mode, each integer represents an uppercase letter: The integer
# modulo 27 indicates the letter of the alphabet (where 1 = A and so on). So an input
# value of 143 in uppercase mode would yield the letter H because 143 modulo 27 is
# 8 and H is the eighth letter in the alphabet.
# The lowercase mode works the same but with lowercase letters; the remainder of
# dividing the integer by 27 represents the lowercase letter (1 = a and so on). So an
# input value of 56 in lowercase mode would yield the letter b because 57 modulo 27
# is 2 and b is the second letter in the alphabet.
# In punctuation mode, the integer is instead considered modulo 9, with the inter-
# pretation given by Table 2-3 below. So 19 would yield an exclamation point because
# 19 modulo 9 is 1.
# At the beginning of each message, the decoding mode is uppercase letters. Each
# time the modulo operation (by 27 or 9, depending on mode) results in 0, the decod-
# ing mode switches. If the current mode is uppercase, the mode switches to lowercase
# letters. If the current mode is lowercase, the mode switches to punctuation, and if it is
# punctuation, it switches back to uppercase


#cycle modes
# Upper -> Lower Case -> Upper Case

# Read character by character until we reach an end-of-line.
#Convert a series of characters representing a number to an integer.
#"Convert an integer 1–26 into an uppercase letter."
#"Convert an integer 1–26 into a lowercase letter." C
#CV onvert an integer 1–8 into a punctuation symbol based on Table 2-3.
*/

#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;




/*
# Track a decoding mode.
*/

main() {

/* real issue is not knowing how many digits will be used
there for, maybe a for loop that for each position of the digit is multipled
by the position and the number of zeros
such as 10 would be posiiton 1 and 1 zer0)




/* this uses one variable, too add 2 digits together */


cout << "Enter a two digit number ";
char digitChar = cin.get();
int overallNumber = (digitChar - '0') * 10;
digitChar = cin.get();
overallNumber += (digitChar - '0' ); /* adding integer value */
cout << "That number as an integer: " << overallNumber << "\n";


/* USing multiple vales to intake 2 digits and add them.
the first digit is multiple by 10 because it is in the tens column */

/*
cout << "enter a two digit number: ";
char digitChar1 = cin.get();
char digitChar2 = cin.get ();
int digit1 = digitChar1 - '0';
int digit2 = digitChar2 - '0';
int overallNumber = digit1 * 10 + digit2;
cout << "That number as an interget: " << overallNumber << "\n";
*/
}