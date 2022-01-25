#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int $;
    cout << " 輸入購物金額：";
    cin >> $;
    cout << " 需要找 " << 1000-$ << " 元" << endl;
    cout << " 找：" << endl;
    cout << " 500 元 " << (1000-$)/500 << " 張" << endl;
    cout << " 100 元 " << (1000-$)%500/100 << " 張" << endl;
    cout << " 50  元 " << (1000-$)%100/50 << " 個" << endl;
    cout << " 10  元 " << (1000-$)%50/25 << " 個" << endl;
    cout << " 5   元 " << (1000-$)%10/5 << " 個" << endl;
    cout << " 1   元 " << (1000-$)%5 << " 個" << endl;
    system("pause");

    return 0;
}
