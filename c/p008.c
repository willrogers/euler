#include <stdio.h>
#include <string.h>

#define LINES 20
#define LENGTH 50
#define TOTAL 1000
#define SEQ 13
#define FILENAME "data/p008_bignumber.txt"

int main () {
	int snum[TOTAL];
	int i,j = 0;
	FILE *fp = fopen(FILENAME, "r");
	char c = fgetc(fp);
	while (c != EOF) {
		if (! isspace((int)c)) {
			snum[i] = c - '0';
			i++;
		}
		c = fgetc(fp);
	}

	unsigned long max = 0;
	unsigned long mult = 1;
	for (i = SEQ; i < TOTAL; i++) {
		mult = 1;
		for (j = 0; j < SEQ; j++) {
			mult *= snum[i - j];
		}
		if (mult > max) {
			max = mult;
		}
	}
	printf("%lu\n", max);
	return 0;
}
