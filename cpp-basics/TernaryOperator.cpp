#include <iostream>

int main(){
    //ternary operator ?: = replacement to if/else statement
    // condition ? expression1 : expression2;
    double attendance =5;
    attendance>=75 ? 
    std::cout << "No grade down\n":
    std::cout<< "Grade Down!!\n \n\n";
    // Another way
    std::cout << (attendance >= 75 ? "No grade down\n":"Grade Down!!\n");
    return 0;
}