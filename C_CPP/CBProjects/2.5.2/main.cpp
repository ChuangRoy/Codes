#include <iostream>
#define PI 3.1415926

using namespace std;

int main()
{
    float radius;
    cout << " 請輸入半徑：";
    cin >> radius;

    cout << " 此圓的面積為 " << PI * radius * radius << endl;
    cout << " 此園的周長為 " << 2 * PI * radius << endl;
    return 0;
}
