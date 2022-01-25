#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    int a;
    int b;
    printf("Input 2 intengers:");
    scanf("%d %d",&a,&b);
    printf("A = %d  B = %d\n",a,b);
    a = a + b;
    b = a - b;
    a = a - b;
    printf("A = %d  B = %d\n",a,b);
    system("pause");

    return 0;
}
