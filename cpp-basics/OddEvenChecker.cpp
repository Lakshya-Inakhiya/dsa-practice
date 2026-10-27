#include <iostream>

int main(){
    int num;
    std::cout <<"Enter a Number:"<<'\n';
    std::cin >> num ;
    if( num % 2 == 0){
        std::cout << "The Number is Even"<<'\n';
    }
    else{
        std::cout << "The Number is Odd"<<'\n';
    }
    return 0;
}