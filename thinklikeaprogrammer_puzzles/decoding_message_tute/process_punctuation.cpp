/*
The punctu-
ation table conversion is not as concise because the punctuation symbols in
the table do not appear in that order in ASCII or any other character code
system. As such, we’re going to have to handle this through brute force:

punctuation rules:
numbesr 1 -8
!?,.<space>;"\

*/

#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;

int main(){

cout << "Enter a Number 1-8 > ";
int number;
cin >> number;
char outputCharacter;
switch (number){ /* Switch statement makes this easiy, corresponds to the number */

    case 1: outputCharacter = '!'; break;
    case 2: outputCharacter = '?'; break;
    case 3: outputCharacter = ','; break;
    case 4: outputCharacter = '.'; break;
    case 5: outputCharacter = ' '; break;
    case 6: outputCharacter = ';'; break;
    case 7: outputCharacter = '"'; break;
    case 8: outputCharacter = '\''; break;

}
cout << "Equivalent symbol: " << outputCharacter << "\n";


}
