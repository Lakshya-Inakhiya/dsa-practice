#include <iostream>

int main(){
    // integer
    int x; // declaration
    x = 13; // assignment
    int y = 5; // both together
    int sum = x + y;
    std::cout << x<< '\n';
    std::cout << y << '\n';
    std::cout << sum << '\n'; // note if u put z = 7.5 . it takes the GIF of it 

    // double (Float in python)
    double sgpasem1 = 8.588;
    double sgpasem2= 6.433;
    double gpa = (sgpasem1 + sgpasem2)/2;
    std::cout << gpa << '\n';

    // char ( single Character)
    char grade = 'F';
    std:: cout << grade << '\n';

    // boolean ( true or false)
    bool student = true;
    bool employed = false;
    std::cout << student << '\n' << employed << '\n';

    // strings
    std::string name = "Lakshya";
    std::cout << "Kya haal h bey " << name << '\n';
    return 0;
}