// Find the sum of Fibonacci numbers which do not 
// exceed 4m.

#include <stdio.h>

#define LIMIT 4000000

int main() {

    int a = 0;
    int b = 1;
    int next = 0;

    int total = 0;

    while (a < LIMIT) {
        printf("a is %d\n", a);
        next = a + b;
        a = b;
        b = next;
        if (a % 2 == 0) {
            total += a;
        }
    }   

    printf("The total is %d\n", total);
        
}
