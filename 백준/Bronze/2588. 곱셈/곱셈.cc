#include <stdio.h>

int main()
{
    int x, y;
    int r1, r2, r3;
    int result;
    
    scanf("%d\n", &x);
    scanf("%d", &y);
    
    r1 = x * (y % 10);
    r2 = x * (y  / 10 % 10);
    r3 = x * (y / 100);
    
    result = x * y;
    
    printf("%d\n", r1);
    printf("%d\n", r2);
    printf("%d\n", r3);
    printf("%d\n", result);

    return 0;
}