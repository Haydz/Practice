#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;


int main(){
const int ARRAY_SIZE = 10;
int gradeArray[ARRAY_SIZE] = {87, 76, 100, 97, 64, 83, 88, 92, 74, 95};
double sum = 0;

for (int i = 0; i < ARRAY_SIZE;  i++) {

    sum += gradeArray[i];

}

double average = sum / ARRAY_SIZE;
cout << average;
}

/*
simple loops through an array until reaches the array size summing all
items iwthin aray. then divides by the length of the array.
*/