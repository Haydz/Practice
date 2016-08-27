#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;

int compareFunc(const void * voidA, const void * voidB){

int * intA = (int *) (voidA);
int * intB = (int *)(voidB);
//cout <<  *intA - *intB;

}

/*
In statistics, the mode of a set of values is the value that appears most often. Write
code that processes an array of survey data, where survey takers have responded to
a question with a number in the range 1–10, to determine the mode of the data set.
For our purpose, if multiple modes exist, any may be chosen.
*/



/*
1) read in an array
2) loop through data counting each value
    start with first, count through all ELEMENTS until end increments count of value
    continue to use second value, count through ALL elements
    continue with 3rd
3)loop through counted elements for the highest counted value
4) if multiple any may be chosen

1st - start with a constraint of 3 values for example not unlimited.
*/



/*
Books teach to sort numbers together first
eg: 11,2,2,2,33,3,3,3,3,3,3,
int surveyData[ARRAY_SIZE] = {4, 7, 7, 9, 9, 9, 8, 3, 3, 3, 3, 10};

*/


/* pseudocode

int mostFrequent = ?;
int highestFrequency = ?;
int currentFrequency = 0;
for (int i = 0; i < ARRAY_SIZE, i++_){

    currentFrequency++;
    if surveyData[i] is last occurance of a value){
     if (currentFrequency > highFrequency){
        highestFrequency = currentFrequency;
        mostFrequency = surveyData[i];
        }
        currentFrequency = 0;
    }




*/
int main(){
const int ARRAY_SIZE = 12;
int surveyData[ARRAY_SIZE] = {4, 7, 3, 8, 9, 7, 3, 9, 9, 3, 3, 10};
//int surveyData[ARRAY_SIZE] = {4, 7, 7, 9, 9, 9, 8, 3, 3, 3, 3, 10};

qsort(surveyData, ARRAY_SIZE, sizeof(int), compareFunc);

//int mostFrequent = surveyData[0];
int mostFrequent;
int highestFrequency = 0;
int currentFrequency = 0;
for (int i = 0; i < ARRAY_SIZE; i ++){
    currentFrequency++;
    // if surveyData[i] is last occurance of a value){
    if (i == ARRAY_SIZE -1 || surveyData[i] != surveyData[i +1]){
        if (currentFrequency > highestFrequency){
            highestFrequency = currentFrequency;
            mostFrequent = surveyData[i];
        }
        currentFrequency = 0;
    }

}
cout << mostFrequent << "\n";
}

