#include <stdio.h>
#include <math.h>

/* return the upper bound on the square root of an integer */
int iroot(int n) {
	double d = (double) n;
	double s = sqrt(d);
	return (int) s + 1;
}

/* return 1 if n is prime, 0 otherwise */
int is_prime(int n) {
	if (n < 2) {
		 return 0;
	}

	/* only need to go up to the root of the number */
        int root = iroot(n);

	int i = 2;
	for (i; i <= root; i++) {
		if (n % i == 0) {
		return 0;
		}
	}
	return 1;
}
