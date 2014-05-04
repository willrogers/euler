/* Find the shortest password that satisfies the password attempts in 
   the file.
*/

#include <stdio.h>
#include <stdlib.h>

#define LINES 50
#define LENGTH 3
#define SL 10

/* The file needs to be of the correct format. 
   Put each character into the array sequentially;
   this function doesn't know that the array is 2D.
*/
char * read_file(char * path, int *  return_array) {
	FILE * f = fopen(path, "r");
	char c;
	int i = 0;
	int next = -1;
	/* Read the file into the array. */
	while ((c = fgetc(f)) != EOF) { 
		if (c != '\n') { 
			//next = atoi(&c);
			next = c - '0';
			*return_array = next;
			printf("array %d is %d from %c\n", i, next, c);
			return_array++;
			
			i++;
		} else {
			printf("\n");
		}
	}
	fclose(f);

}

/* This function DOES know that the array is 2D, so needs 
   dimensions.
*/
void print_array(int start[LINES][LENGTH]) {
	int i, j;
	for (i = 0; i < LINES; i++) {
		for (j = 0; j < LENGTH; j++) { 
			printf("%d", start[i][j]);
		}
		printf("\n");
	}
}


/* Treat the array as 1D */
void print_array2(int * start, int lines) {
	int i, j, index;
	for (i = 0; i < lines; i++) {
		for (j = 0; j < LENGTH; j++) { 
			index = i * LENGTH + j;
			int num = start[index];
			printf("%d", start[index]);
			if (num > 10) {
				printf("What's this? %d\n", num);
			}
		}
		printf("\n");
	}
}

int valid_try(int try, int * line) {
	
//	printf("attempt is %d%d%d\n", line[0], line[1], line[2]);
	char str[SL];
	int j = 0;
	int cur = 0;
	int curc = line[cur];
	sprintf(str, "%d", try);
	/* iterate over the new buffer */
	for (j = 0; j < SL; j++) {
		curc = line[cur];
		int ji = str[j] - '0';
		if (ji == curc) {
			cur++;
		}
	}
	if (cur < 3) {
		return 0;
	} else {
		printf("returning true for %d\n", try);
		printf("attempt was %d%d%d\n", line[0], line[1], line[2]);
		return 1;
	}
}

int main() {
	int arr[3];
	arr[0] = 1;
	arr[1] = 2;
	arr[2] = 3;
	printf("Valid? %d\n", valid_try(123, &arr[0]));
	printf("Valid? %d\n", valid_try(124, &arr[0]));
}

int main1() {

	int tries[LINES][LENGTH];
	char * FILEPATH = "../data/keylog.txt";


	read_file(FILEPATH, &tries[0][0]);
//	print_array(tries, LINES);
	printf("...printing...\n");
	print_array2(&tries[0][0], LINES);
	exit(0);
	int i, j;
	int try = 100;
	while (1) {
		/* LINES matches means success. */
		for (i = 0; i < LINES; i++) {
			if (!valid_try(try, &tries[i][0])) {
				break;	
			}
			printf("i got to %d\n", i);
		}
		if (i == LINES - 1) {
			printf("Matched %d attempts.\n", i);
			printf("The answer is %d\n", try);
			return;
		}
		try++;
	}
}

