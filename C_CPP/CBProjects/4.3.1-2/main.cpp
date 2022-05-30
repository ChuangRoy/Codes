#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int a,b;
    cout << " 請輸入 a b兩數：";
    cin >> a >> b;

    if (a % 2)
        a++;
    if (b % 2)
        b--;

    cout << " a b 之間有 " << (b-a)/2 + 1 << " 個偶數" << endl;

    system("pause");
    return 0;
}
