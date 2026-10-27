#include <iostream>

int main(){
    // for loop
    for( int i = 0; i <10; i += 2 ){
        if(i==4){
            continue;        
        }
        std::cout << i <<'\n';
    }
    return 0;
}