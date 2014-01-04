/* What is the smallest number which is divisible by all of the numbers
   from 1 to 20?
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX_DIVISOR 20

int divides_all(n, max_div) {
	int i = 0;
	for (i=2; i<max_div;i++) {
		if (n % i != 0) {
			return 0;
		} 
	}
	return 1;
}

int main(char *args[]) {
	int test = 10;
	int i = 0;
	while(1) {
		if (divides_all(test, MAX_DIVISOR)) { 
			printf("%d succeeded!\n", test);
			exit(0);
		} else {
			test += 2;
		}
	}	
}
