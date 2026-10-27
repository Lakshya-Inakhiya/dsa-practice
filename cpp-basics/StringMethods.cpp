#include <iostream>

int main(){
    // String Methods
    std::string name;
    std::cout << "Enter Your Name: ";
    std::getline(std::cin, name);
    std::string temp= name;
    std::cout << "string.length outputs: " << name.length()<<'\n';
    std::cout << "string.empty outputs: " << name.empty()<<'\n';
    std::cout << "string.clear clears the string: \n";
    std::cout << "string.append(@gmail.com): "<< temp.append("@gmail.com") <<'\n';
    std::cout << "string.at(1): "<< name.at(1) <<'\n';// index in python
    std::cout << "string.insert(0,@): "<< name.insert(0 , "@") <<'\n';
    std::cout << "string.find(' '): "<< name.find(" ") << '\n';
    std::cout << "string.erase(0 , 1): "<< name.erase(0 , 1)<< '\n';
    // and many more , search on web for use cases
    return 0;
}