#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;



int doubleDigitValue(int digit) {
cout << "GOING THROUGH double digit LOOP";
int doubledDigit = digit * 2;
int sum;
if (doubledDigit > 10) {
sum = 1 + doubledDigit % 10;
}
else{ sum = doubledDigit;
}
return sum;
}




main()
{


char digit;
int oddLengthCheckSum = 0;
int evenLengthCheckSum = 0;

int position =1 ;
cout << "Enter a number: \n";
digit = cin.get ();
char newdigit;
while (digit != 10)
{
	if(position %2 ==0){
	newdigit =digit - '0';
		oddLengthCheckSum += doubleDigitValue(newdigit);
		evenLengthCheckSum += newdigit;
}	else
{
		oddLengthCheckSum += newdigit;
		evenLengthCheckSum += doubleDigitValue(newdigit);
}
	cin.get();
	position ++;
}


int checksum;


/* if checksum has no remainder when divided by 10 its is valid */
if ((position - 1) % 2 == 0) checksum = evenLengthCheckSum;
else checksum = oddLengthCheckSum;
cout << "Checksum is " << checksum << ". \n";
if (checksum % 10 == 0)
{
	cout << "CheckSum is divisable by 10. Valid \n";
} else{
	cout << "CheckSum isn ot divisible by 10, INVALID \n";
}
}



/*
int doubleDigitValue(int digit) {
/* cout << "Enter a single digit number, 0-9 ";
cin >> digit; 

int doubledDigit = digit * 2;
int sum;
if (doubledDigit >=10) sum = 1 + doubledDigit % 10;
else sum = doubledDigit;
cout << "Sum of digits in doubled number: " << sum << "\n"; 
return sum;
}
*/

/* Convert Character digit to integer*/
/*
char digit;
cout << "Enter a one-digit number: ";
cin>> digit;
int sum = digit - '0';
cout << "is the sum of digits " << sum << "? \n";

/* write a program that  takes an identification number of length 6 aand determines
whether the number is valid under Luhn formula 
program must process each cahracter before reading the next one. 
without doubling */

/*
cout << "Enter a six digit number \n";
for (int position = 1; position <= 6; position++) {
cin >> digit;
if (position % 2 == 0) checksum += digit - '0';
else checksum += doubleDigitValue(digit - '0');
}
*/



/* if digit is odd number
double
*/
/*	checksum += digit;  reads each digits 1 by 1 and sums them 
	checksum += digit - '0'; /* because its in character code of 1 is 49
so we must - 48 from char 49 to get 1*/


/*
cout << "Enter a six digit number \n";
for (int position = 0;  position < 6; position++)
{
	cin>> digit;
	cout << "digit is: "<< digit << "\n";
/* convert to number 
digit = digit - '0';

/*if position is odd (every 2nd gets doubled) 

if (position % 2 == 1)
{
sum =  doubleDigitValue(digit);
}else
{ 
cout << "TEST";
}


checksum += sum;
checksum += digit;
*/
/* then add to checksum */


