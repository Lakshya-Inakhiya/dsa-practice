#include <iostream>

int main(){
    // && = and in python
    // || = or in python
    // ! = not in python
    int temp;
    std::cout << "Enter Current Temp: ";
    std::cin >> temp ;
    
    if( temp >=14 && temp <= 40){
        std::cout << "Its Livable normally\n";
    }
    else{
        std::cout << "Its Not livable Normally\n";
    }
    return 0;
}