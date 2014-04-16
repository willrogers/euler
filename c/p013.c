/*
   Find the first ten digits of the sum of the 100 long numbers.
 */

#include <stdio.h>
#include <limits.h>

#define DATA_FILE "../data/longs.txt"
#define LINES 100
#define NUM_LENGTH 50
#define LONG_DIGITS 10
#define MAX_LONG 10000000000

/* define a struct to hold a very large integer */
struct largeint {

	/* Each long holds ten digits.  Lowest values first*/
	long l1;
	long l2;
	long l3;
	long l4;
	long l5;
	long l6;
};

void print_largeint(struct largeint * l) {
	printf("%10ld%10ld%10ld%10ld%10ld%10ld\n", l->l6, l->l5, l->l4, l->l3, l->l2, l->l1); 
}

struct largeint add_largeint(struct largeint li1, struct largeint li2) { 
	struct largeint li;
	long l;
	
	l = li1.l1 + li2.l1;
	if (l > MAX_LONG) { 
		long remainder = l % MAX_LONG;
		int m = l / MAX_LONG;
	}
	
}

long mul_ten_digits(int * array) { 
	int i;
	long current = 0;
	for (i = 0; i < LONG_DIGITS; i++) {
		current = 10 * current + *array;
		array++;
	}
	return current;
}

void parse_file(long long * longs) {
	FILE * f = fopen(DATA_FILE, "r");
	
	char c;
	long long current = 0;
	int digit;
	int i, j;

	int num[NUM_LENGTH];

	/* we know the exact format of the file */
	for (i = 0; i < LINES; i++) { 
		struct largeint lint;
		for (j = 0; j < NUM_LENGTH; j++) {
			c = fgetc(f);
			digit = c - '0';
			printf("%d", digit);
			num[j] = digit;
		}
		printf("\n");
		lint.l5 = mul_ten_digits(&num[0]);
		lint.l4 = mul_ten_digits(&num[10]);
		lint.l3 = mul_ten_digits(&num[20]);
		lint.l2 = mul_ten_digits(&num[30]);
		lint.l1 = mul_ten_digits(&num[40]);
		lint.l6 = 0;
		print_largeint(&lint);

		c = fgetc(f); // newline
		
	}
	
	fclose(f);
		
}

int main() { 
	long long longs[LINES];
	parse_file(&longs[0]);
	printf("sizeof int: %lu.\n", sizeof(int));
	printf("sizeof long: %lu.\n", sizeof(long));
	printf("sizeof long long: %lu.\n", sizeof(long long));
	printf("Max long long: %llu.\n", LLONG_MAX);
}

	
