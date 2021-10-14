#include <stdio.h>
#include <stdlib.h>
const int NUM_BYTES = 8;


int main(){

	FILE *fin;
	FILE *fout;

	int buffer[NUM_BYTES];

	fin = fopen("/dev/random", "r");
	
	if(fin == NULL){
		printf("Error opening /dev/random\n");
		exit(-1);
	}
	
	fout = fopen("random-numbers", "w");
	
	if(fout == NULL){
		printf("Error opening num file\n");
		exit(-1);
	}
	

	int num = 0;
	
	for(int i = 0; i < 1000; i++)
	{

		int countRead = fread(&buffer, sizeof(int), NUM_BYTES, fin);
		
		if(countRead < NUM_BYTES){
			printf("Error reading from /dev/random\n");
			exit(-1);
		}
		
		for(int i = 0; i < NUM_BYTES; i++){
			fprintf(fout, "%x", buffer[i]);	
		}
		fprintf(fout, "\n");


	}

	fclose(fout);
	fclose(fin);

	return 0;
};
