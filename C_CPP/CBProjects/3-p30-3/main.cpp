#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int money;
    cout << " 請輸入消費金額：";
    cin >> money;
    cout << " 需要 " << money - (money / 1000 *100) << " 元" << endl;
    system("pause");
    return 0;
}
