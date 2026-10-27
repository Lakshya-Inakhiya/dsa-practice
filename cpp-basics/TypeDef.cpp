#include <iostream>
#include <vector>

typedef std::vector<std::pair<std::string , int>> pairlist_t;
typedef std::string str;

using text_t = std::string;

int main(){
    // type def: use to give alias for another data type 
    pairlist_t pairlist;
    str Fname = "Lakshya";
    text_t Lname = "Inakhiya";
    std::cout << Fname + Lname <<'\n';
    return 0;
}   