/* Find the 10001st prime number. */

#include "utils.c"
#include <stdio.h>

#define PRIMES 10001

int main(char * args[]) {
	printf("3 is prime: %d\n", is_prime(3));
	int primes[PRIMES] = {0};
	int test = 0;
	int i = 0;
	for (i = 0; i < PRIMES; i++) {
		while (!is_prime(test)) {
			test++;	
		}
		primes[i] = test;
		test++;
	}	


	for (i =0; i < PRIMES; i++) {
		printf("prime %d: %d\n", i+1, primes[i]);
	}
}

