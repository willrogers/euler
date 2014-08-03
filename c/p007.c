/* Find the 10001st prime number. */

#include "utils.c"
#include <stdio.h>

#define PRIMES 10001

int main(char * args[]) {
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


	printf("%d\n", primes[PRIMES]);
	return 0;
}

