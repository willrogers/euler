/*
   On Ubuntu, to include math.h you have to add -lm to gcc.
 */
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
	if (n == 2) {
		return 1;
	}

	/* only need to go up to the root of the number */
	int root = iroot(n);

	int i;
	for (i = 2; i <= root; i++) {
		if (n % i == 0) {
		return 0;
		}
	}
	return 1;
}

/* ints overflow at 13! */
long factorial(int n) {
	if (n == 0) {
		return 1;
	} else {
		int i = 0;
		long total = 1;
		for (i = n; i > 1; i--) {
			total *= i;	
		} 
		return total;
	}
}

/* Pass in a pointer to an array. Assume that there is enough
   room in the array!
   Return the number of factors added to the array.
*/
int factorise(int n, int *factors) {
	int fcount = 0;
	int i = 2;
	while (n > 1) {
		if ((n % i) == 0) {
			*factors = i;		
			n = n / i;
			i = 2;
			factors++;
			fcount++;
		}
		else {
			i++;
		}
	}
	return fcount;
}

