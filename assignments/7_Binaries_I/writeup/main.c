/*
 * Name: Benjamin Chen
 * Section: 0201
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: Benjamin Chen

/* your code goes here */
#include<stdio.h>
#include<stdlib.h>


int main(int argc,char *argv[]){
	
	char *word;
	argv[2] = 0x1ceb00da;
	argv[1] = 0xfeedface;

	int a = argv[1];
	sprintf(word, "%d",a);
	a = NULL;

	a = argv[2];
	sprintf(word, "%d",a);
	a = NULL;

	a = argv[2];
	argv[1] ^= a;
	a = argv[1];
	argv[2] ^= a;
	a = argv[2];
	argv[1] ^= a;

	a = argv[1];
	sprintf(word, "%d",a);
	a = NULL;
}
