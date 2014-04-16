/*
   Find the largest product of numbers in the 4x4 grid.
 */

#include <stdio.h>
#include <stdlib.h>
#define DIMENSION 20

#define DATA_FILE "../data/grid.txt"

/* This currently copies the array. */
void parse_data(int return_array[DIMENSION][DIMENSION]) {

	FILE * file = fopen(DATA_FILE, "r");
	
	return_array[0][0] = 1;	

	char c;
	int d1, d2, d3;
	int i, j;

	for (i = 0; i < DIMENSION; i++) {
		for (j = 0; j < DIMENSION; j++) {
			d1 = fgetc(file) - '0';
			d2 = fgetc(file) - '0';
			d3 = fgetc(file);
			return_array[i][j] = d1 * 10 + d2;
		}
	}


	fclose(file);
}

int main() {
	int a[DIMENSION][DIMENSION] = {0};
	parse_data(a);
	
	int i, j;
	int tot;
	int max = 0;
	/* Horizontally */
	for (i = 0; i < DIMENSION; i++) {
		for (j = 0; j < DIMENSION - 3; j++) {
			tot = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3];
			if (tot > max) { 
				max = tot;
			}
		}	
	}
	/* Vertically */
	for (i = 0; i < DIMENSION - 3; i++) {
		for (j = 0; j < DIMENSION; j++) {
			tot = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j];
			if (tot > max) { 
				max = tot;
			}
		}	
	}
	/* Diag 1 */
	for (i = 0; i < DIMENSION - 3; i++) {
		for (j = 0; j < DIMENSION - 3; j++) {
			tot = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3];
			if (tot > max) { 
				max = tot;
			}
		}	
	}
	/* Diag 2 */
	for (i = 4; i < DIMENSION; i++) {
		for (j = 0; j < DIMENSION - 3; j++) {
			tot = a[i][j] * a[i-1][j+1] * a[i-2][j+2] * a[i-3][j+3];
			if (tot > max) { 
				max = tot;
			}
		}	
	}

	printf("The largest sequence is %d.\n", max);
}

