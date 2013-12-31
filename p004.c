/* Find the largest palindromic number made from the product of 
 * two 3-digit numbers.
 */

#include <stdio.h>

#define MAX_INPUT 1000
#define MAX_LENGTH 6

/* reverse an integer number */
int reverse(int n) { 
	int forward  = n ;
	int integers[MAX_LENGTH] = {0};
	int i = 0;
	/* initialise to -1 */
	for (i; i < MAX_LENGTH; i++) {
		integers[i] = -1;
	}
	for (i = MAX_LENGTH -1; i >= 0; i--) {
		integers[i] = n % 10;
		n /= 10;
		if (n == 0) {
			break;
		}
	}
	int reversed = 0;
	for (i = MAX_LENGTH - 1; i>=0; i--) {
		if (integers[i] == -1) {
			continue;
		} else {
			reversed = reversed * 10 + integers[i];
		}
	}
	return reversed;
}

/* True if the number is a palindrome. */
int is_palindrome(int n) {
	int reversed = reverse(n);
	int x =  (reversed == n);
	return x;
}

int main (int argc, char *argv[]) { 
	int n = 1234;
	
	printf("%d palindromic: %d\n", n, is_palindrome(n));
	n = 0;
	printf("%d palindromic: %d\n", n, is_palindrome(n));
	n = 1111;
	printf("%d palindromic: %d\n", n, is_palindrome(n));

	int max_pal = 0;

	int i = 0;
	int j = 0;
	for (i = 0; i < MAX_INPUT; i++) {
		for (j = 0; j < MAX_INPUT; j++) {
			int x = i * j;
			if (is_palindrome(x)) {
				printf("%d * %d = %d is palindromic\n", i,j,x);
				if (x > max_pal) {
					max_pal = x;
				}
			}
		}
	}
	printf("The biggest palindrome is %d\n", max_pal);
	return 0;
}
