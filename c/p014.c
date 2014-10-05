
#include <stdio.h>
#include <stdlib.h>
/* Use GMP for large integers. */
#include <gmp.h>

#define LIMIT 1000000

static mpz_t q;
static mpz_t coll;

void next_collatz(mpz_t coll, mpz_t q) {
	if (mpz_cdiv_q_ui(q, coll, 2) == 0) {
		mpz_set(coll, q);
	} else {
		mpz_mul_ui(coll, coll, 3);
		mpz_add_ui(coll, coll, 1);
	}
}

int collatz_num(int n) {
	int i = 1;
	mpz_set_si(coll, n);
	do {
		next_collatz(coll, q);
		i += 1;
	} while mpz_cmp_si(coll, 1); 
	return i;
}

int main() {
	int c = 2;
	int max_count = 0;
	int max_coll = 0;
	long i = -1;
	/* initialise mpz_t once for repeated use */
	mpz_init(coll);
	mpz_init(q);
	for (c; c < LIMIT; c++) {
		i = collatz_num(c);
		if (i > max_count) {
			max_count = i;
			max_coll = c;
		}
	}
	printf("%d\n", max_coll);
	/* not really necessary */
	mpz_clear(coll);
	mpz_clear(q);
	return 0;
}

