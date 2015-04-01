/* Find the sum of all the primes below 2 million. */

#include "utils.c"
#include <stdio.h>
#include <stdlib.h>

#define UPPER 2000000

long naive() {
	long total = 2;
	long i = 0;
	for (i = 3; i < UPPER; i += 2) {
		if (is_prime(i)) {
			total += i;
		}
	}
	return total;
}

long array_cancel() {
	int *a = malloc(sizeof(int) * UPPER);
	int i = 0;
	for (i = 2; i < UPPER; i++) {
		a[i] = i;
	}
	for (i = 2; i < UPPER; i++) {
		if (a[i] != 0) {
			int count = 2 * i;
			while (count < UPPER) {
				a[count] = 0;
				count += i;
			}
		}
	}
	long total = 0;
	for (i = 0; i < UPPER; i++) {
		total += a[i];
	}
	return total;
}

int main(int argc, char* args[]) {
	long total = array_cancel();
	printf("%ld\n", total);
	return 0;
}
