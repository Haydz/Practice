/* the numbers come in, and different numbers are seperated
by commmas and end of line.

As such a loop should check for either end of line haracer or a comma.
A larger loop will continue untill all numbers are read,
then the inner loop should only stop for a comma or EOL.

The outer loop stops for EOL when the whole line has finished. */
#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;


int main (){

char digitChar;
do {
    digitChar = cin.get();
    int number = (digitChar - '0' );
    digitChar = cin.get();
    while ((digitChar != 10) && (digitChar != ',')) {
        number = number *10 + (digitChar - '0');
        digitChar = cin.get();
     }
     cout << "numbered Entered: " << number << "\n";



}
while (digitChar != 10);
}