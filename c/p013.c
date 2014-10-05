/*
   Find the first ten digits of the sum of the 100 long numbers.
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>

/* Details of data file */
#define DATA_FILE "longs.txt"
#define LINES 100
#define NUM_LENGTH 50
/* Used for each part of largeint */
#define LONG_DIGITS 10
#define MAX_LONG 10000000000

/* define a struct to hold a very large integer */
struct largeint {
	/* Each long holds ten digits, base 10.  Lowest values first. */
	long l1;
	long l2;
	long l3;
	long l4;
	long l5;
	long l6;
};

struct largeint new_largeint() {
	struct largeint l;
	l.l1 = 0L;
	l.l2 = 0L;
	l.l3 = 0L;
	l.l4 = 0L;
	l.l5 = 0L;
	l.l6 = 0L;
	return l;
}

void print_largeint(struct largeint * l) {
	printf("%10ld%010ld%010ld%010ld%010ld%010ld\n",
		l->l6, l->l5, l->l4, l->l3, l->l2, l->l1);
}

void sprint_largeint(struct largeint * l, char *str) {
	sprintf(str, "%10ld%010ld%010ld%010ld%010ld%010ld\n",
		l->l6, l->l5, l->l4, l->l3, l->l2, l->l1);
}

struct largeint add_largeint(struct largeint li1, struct largeint li2) {
	struct largeint li;
	long l;
	int m = 0;
	
	l = li1.l1 + li2.l1;
	m = l / MAX_LONG;
	l = l % MAX_LONG;
	li.l1 = l;
	l = li1.l2 + li2.l2 + m;
	m = l / MAX_LONG;
	l = l % MAX_LONG;
	li.l2 = l;
	l = li1.l3 + li2.l3 + m;
	m = l / MAX_LONG;
	l = l % MAX_LONG;
	li.l3 = l;
	l = li1.l4 + li2.l4 + m;
	m = l / MAX_LONG;
	l = l % MAX_LONG;
	li.l4 = l;
	l = li1.l5 + li2.l5 + m;
	m = l / MAX_LONG;
	l = l % MAX_LONG;
	li.l5 = l;
	/* we assume l6 won't overflow */
	li.l6 = li1.l6 + li2.l6 + m;
	
	return li;
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

void parse_file(char *filepath, struct largeint * array) {
	FILE * f = fopen(filepath, "r");
	
	char c;
	int digit;
	int i, j;

	int num[NUM_LENGTH];
	/* we know the exact format of the file */
	for (i = 0; i < LINES; i++) {
		struct largeint lint;
		for (j = 0; j < NUM_LENGTH; j++) {
			c = fgetc(f);
			digit = c - '0';
			num[j] = digit;
		}
		lint.l5 = mul_ten_digits(&num[0]);
		lint.l4 = mul_ten_digits(&num[10]);
		lint.l3 = mul_ten_digits(&num[20]);
		lint.l2 = mul_ten_digits(&num[30]);
		lint.l1 = mul_ten_digits(&num[40]);
		lint.l6 = 0;
		array[i] = lint;

		c = fgetc(f); // newline
	}
	fclose(f);
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <data directory>\n", argv[0]);
		return 1;
	}
	// construct correct path
	char* filepath = calloc(strlen(argv[1]) + strlen(DATA_FILE) + 2, sizeof(char));
	strcat(filepath, argv[1]);
	strcat(filepath, "/");
	strcat(filepath, DATA_FILE);

	long long longs[LINES];
	struct largeint lints[LINES];
	parse_file(filepath, &lints[0]);

	int i;
	struct largeint total = new_largeint();
	for(i = 0; i < LINES; i++) {
		total = add_largeint(total, lints[i]);	
	}
	// Now print the first ten numbers from the largeint
	char *str = calloc(61, sizeof(char));
	sprint_largeint(&total, str);
	i = 0;
	while(str[i] == ' ') {
		i+= 1;
	}
	int lim = i + 10;
	for (i; i < lim; i++) {
		printf("%c", str[i]);
	}
	printf("\n");
	// for neatness
	free(str);
	free(filepath);
	return 0;
}
