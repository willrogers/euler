
/* We need to find the triangle number with over 500 divisors.
   To find the divisors of a number, factorise.  You can then
   construct divisors from the factors.
*/

#include "utils.c"
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#define MAX_FACTORS 100000


/* indices is the array of indices used to pick combinations:
  (0,1,2)
  (0,1,3)
  (0,1,4)
  (0,2,3)
  (0,2,4)
  (0,3,4)
  ...
  return 0 if no further possibilities; 1 otherwise
*/
int update_indices(int *indices, int length, int selection) {
	int i = 0;
	int j = 0;
	/* shift the right-hand number first, then move left */
	for (i = selection - 1; i >= 0; i--) {
		/* is the number the maximum for that position? */
		if (indices[i] < length + i - selection) {
			indices[i]++;
			int x = indices[i];
			/* if a number's been incremented, update those
			   to the right
			*/
			for (j = i + 1; j < selection; j++) {
				indices[j] = ++x;	
			}
			return 1;
		}
	}
	return 0;
}

void combinations(int *input_array, int length, int selection, int *result_array) {
	/* result_array is [selection][no-of-combinations] */
	/* allocate memory for indices array */
	int * indices = malloc(sizeof(int) * selection);
	/*initialise*/
	int i = 0;
	int j = 0;
	for(i = 0; i < selection; i++) {
		indices[i] = i;
	}
	
	i = 0;
	do {
		/* fill in the array from the indices in the
		   indices array
		*/
		for(j = 0; j < selection; j++) {
			result_array[i*selection + j] = input_array[indices[j]];
			}
		i++;
	} while (update_indices(indices, length, selection));
	
	free(indices);
}

long ncr(int n, int r) {
	return factorial(n) / factorial(r) / factorial(n - r);
}

/* return the number of unique elements in the array */
int unique_elements(int *array, int length) {
	/* calloc initialises with zeros */
	int *uniques = calloc(length, sizeof(int));
	int i = 0;
	int j = 0;
	int next = 0;
	int nextd = 0;
	for (i = 0; i < length; i++) {
		next = array[i];
		for (j = 0; j < length; j++) {
			nextd = uniques[j];
			if (nextd == 0) {
				uniques[j] = next;
				break;
			} else if (nextd == next) {
				break;
			}
		}
	}
	int k = 0;
	while (uniques[k] != 0) {
		k++;
	}
	free(uniques);
	return k;
}

/* return the number of divisors of n */
int divisors(int n) {
	int factors[MAX_FACTORS] = {0};
	int fcount = factorise(n, factors);
	/* construct all divisors from factors */
	int divisors[MAX_FACTORS] = {0};
	int dcount = 0;

	int i = 0;
	int j = 0;
	int k = 0;
	for (i = 0; i <= fcount; i++) {
		// do one loop of the multiplications:
		int selection = i;
		int ncombs = (int) ncr(fcount, selection);
		int *result_array = malloc(selection*ncombs*sizeof(int));
//		int *prod_array = malloc(ncombs*sizeof(int));
		combinations(factors, fcount, selection, result_array);

		for(j = 0; j < ncombs; j++) {
			int prod = 1;
			for (k = 0; k < selection; k++) { 
				prod *= result_array[k+j*selection];
			}
//			prod_array[j] = prod;
			divisors[dcount++] = prod;
		}
		free(result_array);
//		free(prod_array);
	}
	
	int ue = unique_elements(divisors, dcount);
	return ue;
}

int main() {
	int d = 0;
	int ntriangle = 1;
	int triangle = 1;
	
	/* construct triangle numbers and check the number of divisors */
	while (d < 500) {
		triangle += ++ntriangle;
		d = divisors(triangle);
	}	
	
	printf("Triangle number %d has %d divisors\n", triangle, d);
	return 0;
}
