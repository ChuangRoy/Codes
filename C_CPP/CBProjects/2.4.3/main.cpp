#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    float radius;
    cout << " 請輸入半徑：";
    cin >> radius;

    cout << " 此圓的面積為 " << 3.14 * radius * radius << endl;
    cout << " 此園的周長為 " << 2 * 3.14 * radius << endl;
    return 0;
}
