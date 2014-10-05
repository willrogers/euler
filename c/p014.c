
#include <stdio.h>
#include <stdlib.h>
/* Use GMP for large integers. */
#include <gmp.h>

#define LIMIT 1000000

void next_collatz(mpz_t out, const mpz_t in) {
	mpz_t q;
	mpz_init(q);
	if (mpz_cdiv_q_ui(q, in, 2) == 0) {
		mpz_set(out, q);
	} else {
		mpz_mul_ui(out, in, 3);
		mpz_add_ui(out, out, 1);
	}
	mpz_clear(q);
}

int collatz_num(int n) {
	int i = 1;
	mpz_t coll;
	mpz_init(coll);
	mpz_set_si(coll, n);
	mpz_t next;
	mpz_init(next);
	do {
		mpz_set_si(next, 0L);
		next_collatz(next, coll);
		mpz_set(coll, next);
		i += 1;
	} while mpz_cmp_si(coll, 1); 
	mpz_clear(coll);
	mpz_clear(next);
	return i;
}

int main() {
	int c = 2;
	int max_count = 0;
	int max_coll = 0;
	long i = -1;
	for (c; c < LIMIT; c++) {
		i = collatz_num(c);
		if (i > max_count) {
			max_count = i;
			max_coll = c;
		}
	}
	printf("%d\n", max_coll);
	return 0;
}

