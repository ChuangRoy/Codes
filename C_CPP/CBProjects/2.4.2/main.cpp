#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    char c;
    int a;

    cout << " 請輸入一個字元：";
    cin >> c;
    a = c;
    cout << " 此字元的ASCII碼是" << a << endl << endl;

    cout << " 請輸入一個ASCII碼：";
    cin >> a;
    c = a;
    cout << " 此ASCII碼的字元是" << c << endl << endl;

    cout << a + c << endl;
    return 0;
}
