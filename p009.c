/* Find the Pythagorean triplet for which a + b + c = 1000. */

#define SIZE 1000
#include <stdio.h>
#include <math.h>

int is_triplet(a, b, c) {
	return (a * a + b * b == c * c );
}

int main () {

	int numbers[SIZE] = {0};
	int squares[SIZE] = {0};

	int i = 0;
	for (i; i < SIZE; i++) { 
		numbers[i] = i;
		squares[i] = i * i;	
	}	
	
	printf("%d,%d,%d: %d\n", 1, 2, 3, is_triplet(1,2,3));
	printf("%d,%d,%d: %d\n", 1, 2, 3, is_triplet(3,4,5));
	printf("%d; sqrt %f\n", 10, sqrt((double)10));
	return 0;
}
