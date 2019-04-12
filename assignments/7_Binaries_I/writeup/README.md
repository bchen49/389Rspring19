# Writeup 7 - Binaries I

Name: Benjamin Chen
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Benjamin Chen

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
```c
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
```

### Part 2 (10 Pts)

The program achieves a form of encryption by xoring text with a key.