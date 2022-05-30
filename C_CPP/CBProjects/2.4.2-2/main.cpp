#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    char ch;
    cout << " 請輸入一個小寫字母：";
    cin >> ch;

    cout << " 此字母的大寫為" << char(ch - 32) << endl;

    return 0;
}
