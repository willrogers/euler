/* Find the Pythagorean triplet for which a + b + c = 1000. */

#include <stdio.h>
#include <math.h>

#define SIZE 1000
#define TRIPLES 10000

int is_triplet(a, b, c) {
	return (a * a + b * b == c * c );
}

int in(int value, int array[SIZE]) {
	int i =0;
	for (i=0; i<SIZE; i++) {
		if (value == array[i]) {
			printf("value is %d\n", value);
			return i;
		}
	}
	return 0;
}

int main () {

	printf("happening?\n");
	int numbers[SIZE] = {0};
	int squares[SIZE] = {0};

	int count = 0;
	int triples[TRIPLES][3] = {0};

	int i,j = 0;
	for (i = 0; i < SIZE; i++) { 
		numbers[i] = i;
		squares[i] = i * i;	
	}	
	for (i=1; i<SIZE; i++) {
		for (j=1; j<SIZE; j++) {
			int x = i * i + j * j;
			int y = in(x, squares);
			if (y) {
				triples[count][0] = i;
				triples[count][1] = j;
				triples[count][2] = y;
				count++;
				printf("i, j, k %d %d %d\n", i, j, y);
			}
		}
	}
	printf("happening?\n");
	for (i=0; i < count; i++) {
		int x = triples[i][0];
		int y = triples[i][1];
		int z = triples[i][2];
//		printf("%d %d %d\n", x, y, z);
		if (x + y + z == 1000) {
			printf("  success! %d %d %d\n", x, y, z);
		}
	}
	return 0;
}
