#include <iostream>

int main(){
    // nested loop
    /*
        loop(){
            loop(){
        
            }
        }
    */
    for(int i = 1 ; i<=5;i++){
        for(int j = 1 ; j<=i;j++){
            std::cout << j;
        }
        std::cout << '\n';
    }
}