#include <iostream>

using namespace std;

int main()
{
    int p,y;
    float r,p_plus_r;

    cout << " 輸入本金 利息(%) 年 ：";
    cin >> p >> r >> y;
    r /= 100;

    int i;
    for (i=0;i<=y,i++) {
        cout << " 第 " << y << "年 ："
        p_plus_r += p*r;
        cout << " p = " << p;
    }
    return 0;
}
