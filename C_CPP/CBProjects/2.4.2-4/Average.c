#include <stdio.h>
#include <stdlib.h>

int main()
{
    int Chinese,English,Math;
    printf(" 請輸入國文、英文、數學三科成績：");
    scanf("%d %d %d",&Chinese,&English,&Math);
    float Average = (Chinese+English+Math)/3;
    printf(" 國文\t英文\t數學\t平均\t是否及格\n");
    printf(" %d\t%d\t%d\t%f",Chinese,English,Math,Average);
    (Average >= 60)?printf("\t是"):printf("\t否");
	system("pause");
    return 0;
}
