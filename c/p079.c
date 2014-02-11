/* Find the shortest password that satisfies the password attempts in 
   the file.
*/

#include <stdio.h>

#define LINES 50
#define LENGTH 3

/* The file needs to be of the correct format. */
char * read_file(char * path, int *  return_array) {
	FILE * f = fopen(path, "r");
	int c;
	int i = 0;
	/* Read the file into the array. */
	while ((c = fgetc(f)) != EOF) { 
		if (c != '\n') { 
			*return_array = atoi(&c);
			printf("array %d is %d\n", i, atoi(&c));
			return_array++;
			
			i++;
		} else {
			printf("\n");
		}
	}
	fclose(f);

}

int main() {

	int tries[LINES][LENGTH];
	char * FILEPATH = "../data/keylog.txt";


	read_file(FILEPATH, &tries[0][0]);
	int i, j;
	for (i = 0; i < LINES; i++) {
		for (j = 0; j < LENGTH; j++) { 
			printf("%d", tries[i][j]);
		}
		printf("\n");
	}
	
	printf("The first number is %d\n", tries[0][0]);
	printf("The last number is %d\n", tries[LINES-1][LENGTH-1]);

	printf("Finished.\n");
}

