#include <iostream>

int main(){
    //taking input
    std::string name;
    std::getline(std::cin >> std::ws, name);
    std::cout << "your name is " << name<<'\n' ;
    std::string fname;
    std::getline(std::cin, fname);
    std::cout << "your full name is " << fname <<'\n';
    return 0;
}