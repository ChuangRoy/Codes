#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    const double pi = 3.1415926;
    float radius;
    cout << " 請輸入半徑：";
    cin >> radius;

    cout << " 此圓的面積為 " << pi * radius * radius << endl;
    cout << " 此園的周長為 " << 2 * pi * radius << endl;
    return 0;
}

