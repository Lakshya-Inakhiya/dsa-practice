#include <iostream>

namespace anime{
    std::string fav = "Eren Yeager";
}
namespace  live{
    std::string fav = "Raymond Reddinton";
}
int main(){
    // const keyword specifies that a variables value is constant 
    // prevent from modifing it

    const double  PI = 3.14159;
    double r;
    r = 13;
    double circumference = 2 * PI * r ;
    std::cout << "Circumference of radius "<<r<<" units is "<<circumference<<" units\n";

    /*
    namespace: provides a solution for preventing name conflicts
    each entity needs a unique name . 
    a namespace allows identical named entities as long as they have different 
    namespace
    */

    std::cout << anime::fav <<'\n';
    std::cout << live::fav <<'\n';

    using namespace anime;
    std::cout << fav <<'\n';
    
    std::string fav = "Raymond Reddinton Always";
    std::cout << fav <<'\n';
    return 0;
}