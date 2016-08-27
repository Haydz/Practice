#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;


int main(){

/*
This is easy to modify sorting with i

/*

works like sorting cards, pick cards up one at a time and insert them in
the appropriate place. moving other cards down to make room

2 variables are declared, -start end, these are 1st and last
subscript of the elemnts in array.
Outer loop selects next card to be inserted into sorting hand.

Loop starts at i +1 as to start loop with 2nd item to compare against
first.

The inner loop places current value in correct position by
repeateatdly swapping current value with predecessory
until reaching correct location.

Look counter j starts at i, look decrements j so long as have not reached
low enbd of array and havent yet found right stopping point.

Until then 3 3 statements to swap the current value down one position.
moving until the left card is greater than current card.


*/

int start = 0;
int end = ARRAY_SIZE - 1;
for (int i = start + 1; i <= end; i ++){
    for(int j = i; j > start && intArray[j-1] > intArray[j]; j--)
    {
    int temp = intArray[j-1];
    intArray[j-1] = intArray[j];
    intArray[j] = temp;
    }

    }

    }