#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main_disabled()
{
    int year;
    int a;
    bool leap_year;
    cout << " 輸入西元年(負數會強制轉正): ";
    cin >> year;
    year = abs(year);
    cout << " 西元 " << year << " 年" << endl;
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0)
                leap_year = 1;
            else
                leap_year = 0;
        }else
            leap_year = 1;
    }else
      leap_year = 0;


    if (leap_year)
        cout << " 閏年";
    else
        cout << " 平年";

    cout << endl;
    system("pause");
    return 0;

}
