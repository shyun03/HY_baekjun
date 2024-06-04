#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main(void)
{
	int a;
	int b;
	int result;

	scanf("%d %d", &a, &b);

	result = a - b;

	printf("%d", result);

	return 0;

}