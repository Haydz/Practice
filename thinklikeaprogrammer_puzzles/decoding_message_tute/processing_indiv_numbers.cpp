/*
Convering a number 1-26 to a letter A-Z.

is basically a reversal process of converting a digit character to the integer equivalent
*/

#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;

int main(){

cout << "Enter a Number 1-26> ";
int number;
cin >> number;
char outputCharacter;
outputCharacter = number + 'A'; /* this is adding the char A (65 decimal) to the integer) */
cout << "Equivalent Symbol: " << outputCharacter   << "\n";

/* the idea is that the integer is added together with the decimal version of the char, but then
the sum is represented as a characer
This works because the digit 0 will be the letter A in this puzzle "

}