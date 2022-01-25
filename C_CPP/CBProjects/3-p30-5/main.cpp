#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    float w1,w2,h;
    cout << " 請輸入上底、下底、高：";
    cin >> w1 >> w2 >> h;
    cout << " 面積 " << (w1+w2)*h/2 << endl;
    system("pause");
    return 0;
}
