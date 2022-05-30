#include <iostream>

using namespace std;

int main()
{
    int a,b,c;
    double m,p;
    cout << "Input the length of the three sides of the triangle:";
    cin >> a >> b >> c;

    if ((a+b>c) && (b+c>a) && (a+c>b)){
        m = 0.5 * (a + b + c);
        p = m * (m-a) * (m-b) * (m-c);
        cout << "It cost $" << p << endl;
    }else
        cout << a << b << c << "can't b a triangle" << endl;

    return 0;
}
