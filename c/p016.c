
#include <math.h>
/* Use GMP for large integers. */
#include <gmp.h>
#include <stdio.h>

#define EXPONENT 1000


int main() {
	mpz_t num, base, dummy;
	mpz_init(num);
	mpz_init(dummy);
	mpz_init_set_ui(base, 2);
	/* GMP exponentiation. */
	mpz_pow_ui(num, base, EXPONENT);

	int next_digit;
	long total = 0;
	while (mpz_cmp_ui(num, 0)) {
		next_digit = mpz_tdiv_r_ui(dummy, num, 10);
		total += next_digit;
		mpz_tdiv_q_ui(num, num, 10);
	}
	printf("%d\n", total);
	return 0;
}
