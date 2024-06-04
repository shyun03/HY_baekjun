#include <stdio.h>

int main()
{
    int x, y=0;
    for (int i = 0; i <5; i++) {
        scanf("%d", &x);
        y += x;
    }
    printf("%d", y);
    return 0;
}