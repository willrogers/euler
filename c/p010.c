/* Find the sum of all the primes below 2 million. */

#include "utils.c"
#include <stdio.h>

#define UPPER 2000000

int main(char* args[]) {
	
        long total = 2;
        int i = 0;
        for (i=3; i<UPPER; i+=2) {
                if (is_prime(i)) {
		//	printf("prime: %d\n", i);
                        total += i;
                }
        }
        printf("The total is %ld\n", total);
}

