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
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0) {
                cout << " 閏年" << endl;
                goto jmp;
            }
            cout << " 平年" << endl;
            goto jmp;
        }
      cout << " 閏年" << endl;
      goto jmp;
    }else {
      cout << " 平年" << endl;
    }
    jmp:
    return 0;

}
