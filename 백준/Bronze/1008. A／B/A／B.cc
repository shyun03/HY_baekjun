#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main(void)
{
	int a;
	int b;
	double result;

	scanf("%d %d", &a, &b);

	result = (double)a / b;

	printf("%.9f", result);

	return 0;

}