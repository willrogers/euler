// Find the largest prime factor of 600851475143.

#include <stdio.h>

//#define UPPER 13195
#define UPPER 600851475143

int is_prime(int n) {
    if (n < 2) { 
        return 0;
    }
    
    int i = 2;
    for (i; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
    
}

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

    int k = 0;
    for (k; k < no_factors; k++) {
        if (factors[k] == 0) {
            break;
        }
        printf("Item %d is %d\n", k, factors[k]);
    }
}
