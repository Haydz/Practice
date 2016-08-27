#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;

int start = 0;
int end = ARRAY_SIZE - 1;
for (int i = start + 1; i <= end; i ++){
    for(int j = i; j > start && intArray[j-1] > intArray[j]; j--)
    {
    int temp = intArray[j-1];
    intArray[j-1] = intArray[j];
    intArray[] = temp;
    }

    }