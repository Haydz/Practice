#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;



int compareFunc(const void * voidA, const void * voidB){

int * intA = (int *) (voidA);
int * intB = (int *)(voidB);
cout <<  *intA - *intB;

}




int main(){



const int ARRAY_SIZE = 10;
int intArray[ARRAY_SIZE] = {87,28,100,78,1,2,3,4,5,7};
qsort(intArray, ARRAY_SIZE, sizeof(int), compareFunc);

/*
qsort takes 4 parameters
array to be sorted
number of elements in array
size of one element in array, determined by sizeof(int)
and the comparator function

Function is passed itself, not called the function.

*/


}