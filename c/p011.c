/*
   Find the largest product of numbers in the 4x4 grid.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DIMENSION 20
#define DATA_FILE "grid.txt"

/* This currently copies the array. */
void parse_data(char *data_file, int return_array[DIMENSION][DIMENSION]) {

	FILE * file = fopen(data_file, "r");

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

int main(int argc, char*argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <data directory>\n", argv[0]);
		return 1;
	}
	int a[DIMENSION][DIMENSION] = {0};
	// construct correct path
	char* filepath = calloc(strlen(argv[1]) + strlen(DATA_FILE) + 2, sizeof(char));
	strcat(filepath, argv[1]);
	strcat(filepath, "/");
	strcat(filepath, DATA_FILE);
	parse_data(filepath, a);
	
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
	printf("%d\n", max);
	return 0;
}

