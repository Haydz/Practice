#include <iostream>
#include <stdlib.h>
using std::cin;
using std::cout;


int main(){
double grossSales = 70000.0;
const int NUM_CATEGORIES = 4;
const double categoryThresholds[NUM_CATEGORIES] = {0.0, 50000.0, 150000.0, 500000.0};
const double licenceCost[NUM_CATEGORIES] = {50.0, 200.0, 1000.0, 5000.0};

int category = 0;
while (category < NUM_CATEGORIES && categoryThresholds[category] <= grossSales){
    category++;


}
double cost = licenceCost[category -1];

cout <<"with sales of " << grossSales << " the licence cost is : " << cost <<"\n";
}