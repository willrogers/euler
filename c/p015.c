/*
 * At any point the number of routes is the sum of the routes to
 * the point above and the point to the left.
 */
#include <stdio.h>

/* A 20x20 grid has 21x21 vertices. */
#define GRID_SIZE 21

int main() {
	long grid[GRID_SIZE][GRID_SIZE] = {0};
	long i, j;
	for (i = 0; i < GRID_SIZE; i++) {
		grid[i][0] = 1;
		grid[0][i] = 1;
	}

	for (i = 1; i < GRID_SIZE; i++) {
		for (j = 1; j < GRID_SIZE; j++) {
			grid[i][j] = grid[i-1][j] + grid[i][j-1];
		}
	}

	printf("%ld\n", grid[GRID_SIZE-1][GRID_SIZE-1]);
	return 0;
 }
