/* Find the difference between the sum of the squares and the square of 
   the sum of the first 100 natural numbers.
*/

#define MAX 100
#include <stdio.h>

int main(char* args[]) {
	int i = 0;
	int sum_squares = 0;
	int sum = 0;
	for (i = 1;  i < MAX + 1; i++) {
		sum += i;
		sum_squares += i*i;
	}
	printf("Answer: %d\n", (sum*sum - sum_squares));
}
