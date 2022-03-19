#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int a,b;
    for (a=2;a<=9;a++) {
        for (b=2;b<=9;b++)
            cout << a << "*" << b << "=" << a*b << " \t";
        cout << endl;
    }

    system("pause");
    return 0;
}
