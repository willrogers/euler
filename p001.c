// Find all the multiples of 3 or 5 below 1000.

#include <stdio.h>

int main() {

    int i = 0;
    int total = 0;
    for (i; i < 1000; i++) { 
       if ((i % 3 == 0) || (i % 5 == 0)) {
            total += i;
        } 
    }
    
    printf("The total is: %d\n", total);
}
