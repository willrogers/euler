#include <stdio.h>
#include <string.h>

#define LINES 20
#define LENGTH 50
#define TOTAL 1000
#define SEQ 5

int main () {

	/* This wasn't a good way to do it. */
	char s1[LENGTH] = "73167176531330624919225119674426574742355349194934";
	char s2[LENGTH] = "96983520312774506326239578318016984801869478851843";
	char s3[LENGTH] = "85861560789112949495459501737958331952853208805511";
	char s4[LENGTH] = "12540698747158523863050715693290963295227443043557";
	char s5[LENGTH] = "66896648950445244523161731856403098711121722383113";
	char s6[LENGTH] = "62229893423380308135336276614282806444486645238749";
	char s7[LENGTH] = "30358907296290491560440772390713810515859307960866";
	char s8[LENGTH] = "70172427121883998797908792274921901699720888093776";
	char s9[LENGTH] = "65727333001053367881220235421809751254540594752243";
	char s10[LENGTH] = "52584907711670556013604839586446706324415722155397";
	char s11[LENGTH] = "53697817977846174064955149290862569321978468622482";
	char s12[LENGTH] = "83972241375657056057490261407972968652414535100474";
	char s13[LENGTH] = "82166370484403199890008895243450658541227588666881";
	char s14[LENGTH] = "16427171479924442928230863465674813919123162824586";
	char s15[LENGTH] = "17866458359124566529476545682848912883142607690042";
	char s16[LENGTH] = "24219022671055626321111109370544217506941658960408";
	char s17[LENGTH] = "07198403850962455444362981230987879927244284909188";
	char s18[LENGTH] = "84580156166097919133875499200524063689912560717606";
	char s19[LENGTH] = "05886116467109405077541002256983155200055935729725";
	char s20[LENGTH] = "71636269561882670428252483600823257530420752963450";

	int num = 0;
	/* 20 * LENGTH array */
	int all[LINES][LENGTH] = {0};
	int i, j = 0;
	for (i = 0; i < LENGTH; i++) { 
		/* whoops */
		all[0][i] = s1[i] - '0';	
		all[1][i] = s2[i] - '0';	
		all[2][i] = s3[i] - '0';	
		all[3][i] = s4[i] - '0';	
		all[4][i] = s5[i] - '0';	
		all[5][i] = s6[i] - '0';	
		all[6][i] = s7[i] - '0';	
		all[7][i] = s8[i] - '0';	
		all[8][i] = s9[i] - '0';	
		all[9][i] = s10[i] - '0';	
		all[10][i] = s11[i] - '0';	
		all[11][i] = s12[i] - '0';	
		all[12][i] = s13[i] - '0';	
		all[13][i] = s14[i] - '0';	
		all[14][i] = s15[i] - '0';	
		all[15][i] = s16[i] - '0';	
		all[16][i] = s17[i] - '0';	
		all[17][i] = s18[i] - '0';	
		all[18][i] = s19[i] - '0';	
		all[19][i] = s20[i] - '0';	
	}
	printf("%d\n", all[LINES-1][LENGTH-1]);
	printf("%d\n", all[1][1]);
	/* stores the current 5 numbers */
	int running[SEQ] = {0};
	int best = 0;
	int try = 0;
	int next = 0;
	for (i = 0; i < TOTAL; i++) {
		/* the right number in the array */
		next = all[i / LENGTH][i % LENGTH];
		try = 1;
		/* shift the current number array */
		for (j = 0; j < SEQ - 1; j++) { 
			running[j] = running[j+1];
			printf("%d * ", running[j]);
			try *= running[j];
		} 
		printf("%d ", next);
		try *= next;
		printf(" try is %d\n", try);
		running[SEQ-1] = next;
		if (try > best) {
			best = try;
		}
		//num++;
	}
	printf("Best is %d\n", best);
//    strcpy(nums, s2);
//    printf("%s\n", s2);
//    strcpy(nums, s2);
 //   printf("%s\n", nums);
}
