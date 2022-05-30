#include <iostream>

using namespace std;

int main()
{
    float radius;
    float height;
    cout << " 請輸入半徑(cm)：";
    cin >> radius;

    cout << endl << " 請輸入柱高(cm)：";
    cin >> height;

    cout << " 半徑 " << radius  << " cm " << " 柱高 " << height << " cm";
    cout << " 體積：" << radius * radius * 3.14 * height;
    cout << " 表面積：" << (radius * radius * 3.14) * 2 + (radius * 2 * 3.14 * height);
    return 0;
}
