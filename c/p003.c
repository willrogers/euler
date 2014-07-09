// Find the largest prime factor of 600851475143.

#include "utils.c"
#include <stdio.h>

#define UPPER 600851475143

int main() {

    int no_factors = 20;
    int factors[no_factors];
    int i = 0;
    for (i; i < no_factors; i++) {
        factors[i] = 0;   
    }
    int * fp = factors;
    
    long long factorise = UPPER;
   
    int j = 2;
    while (factorise > 1) {
        if (is_prime(j)) {
            while (factorise % j == 0) {
                *fp = j;
                fp++;
                factorise /= j;
            }
        }
        j++;
    } 

    int max = 0;
    int k = 0;
    int next = 0;
    for (k; k < no_factors; k++) {
        next = factors[k];
        if (next == 0) {
            break;
        } else if (next > max) {
            max = next;
        }
    }
    printf("The biggest prime factor is %d\n", max);
}
