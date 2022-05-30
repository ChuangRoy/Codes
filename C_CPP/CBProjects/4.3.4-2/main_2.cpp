#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    int year;
    int a;
    cout << " 輸入西元年(負數會強制轉正): ";
    cin >> year;
    year = abs(year);
    cout << " 西元 " << year << " 年" << endl;
    ((year % 400 == 0) || ((year % 100 != 0) && (year % 4 == 0)))?cout << " 閏年":cout << " 平年";
    cout << endl;
    system("pause");
    return 0;

}
