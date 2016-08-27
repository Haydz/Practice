#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;



int main(){



const int ARRAY_SIZE = 10;
int countNegative = 0;
int vendor_payments[ARRAY_SIZE] = {1,2,3,4,5,6,7,8,9,-1};

for (int i = 0; i < ARRAY_SIZE; i++){
    if (vendor_payments[i] < 0) countNegative++;
    }

cout << countNegative << "\n";


}