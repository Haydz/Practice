/*histogram code
This is to create a 2nd array of the 1st array

The makes the code more efficient

*/
#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;

/*

The idea here is that all values are initialized to zero
then ready to count the occurances of each
value in survey data with the other loop.
*/
int main(){

const int ARRAY_SIZE = 12;
int surveyData[ARRAY_SIZE] = {4, 7, 3, 8, 9, 7, 3, 9, 9, 3, 3, 10};
int mostFrequent = 0;
int highestFrequency = 0;
int currentFrequency = 0;

const int MAX_RESPONSE = 10;
int histogram[MAX_RESPONSE];

for (int i = 0; i < MAX_RESPONSE; i++){
    histogram[i] = 0;
    }
for (int i = 0; i < ARRAY_SIZE; i++){
    histogram[surveyData[i] -1]++; //ready to count the ouccurances.
}

for (int i =1; i < MAX_RESPONSE; i++){
    if( histogram[i] > histogram[mostFrequent]) mostFrequent = i;
    }
mostFrequent++;
cout << surveyData[mostFrequent];
}