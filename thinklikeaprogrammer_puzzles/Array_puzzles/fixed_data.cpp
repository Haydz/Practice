#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;
//OWN loop for iterating through fixed array

int main(){
int ARRAY_SIZE = 5;
int test [ARRAY_SIZE] = {1,2,3,4,0};

const char punctuation[8] = {'!', '?', ',', '.', ' ', ';', '"', '\''};
//outputCharacter = punctuation;

for (int i =0; i < ARRAY_SIZE; i++  ){

    cout << test[i] << " in punctuation is decoding " << punctuation[test[i]] << "\n";



}
//converting punctuation into number



char targetValue = '?';
const int ARRAY_SIZES = 8;

//below array is not needed because it is actually comparing
// puntucation code above abouts the target value in order to turn it into
// the correct number
//const char testing[ARRAY_SIZES] = {'!','!',',','.','"',',',',','?'};

int targetPos = 0;
while (punctuation[targetPos] != targetValue && targetPos < ARRAY_SIZES)
    targetPos++;

int punctuationCode = targetPos +1;
cout << punctuationCode << "\n";




}