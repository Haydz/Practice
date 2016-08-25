/*PROBLEM: READING A NUMBER WITH THREE OR
FOUR DIGITS
Write a program to read a number character by character and convert it to an inte-
ger, using just one char variable and one int variable. The number will have either
three or four digits*

/*

PROBLEM: READING A NUMBER WITH THREE OR
FOUR DIGITS, FURTHER SIMPLIFIED
Write a program to read a number character by character and convert it to an inte-
ger, using just one char variable and two int variables. The number will have either
three or four digits.
*/

#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;




main(){
cout << "Enter a number with as many digits as you like> ";
char digitChar = cin.get();
int number = (digitChar - '0');
digitChar = cin.get();
while (digitChar != 10) {
    number = number *10 + (digitChar - '0');
    digitChar = cin.get();
}
cout << "Numbered Entered : " << number << "\n";



/* long way to do it */

/*
cout << "enter a 3 digit or 4 digit number or 5: ";
char digitChar = cin.get();
int number = (digitChar - '0') *100;
digitChar = cin.get();
number += (digitChar - '0') *10;
digitChar = cin.get();
number += (digitChar - '0');
digitChar = cin.get();
if (digitChar == 10){
    cout<< "numbered entered: "<< number << "\n";
}else {
    number = number * 10 + (digitChar - '0');
    digitChar = cin.get();
   }

if (digitChar == 10){
    cout<< "numbered enter ed: "<< number << "\n";
}else {
    number = number * 10 + (digitChar - '0');
    cout << "Numbered entered: " << number << "\n";
   }
*/
}
