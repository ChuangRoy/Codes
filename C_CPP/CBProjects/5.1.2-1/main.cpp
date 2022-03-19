#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    cout << "*|   1\t2\t3\t4\t5\t6\t7\t8\t9\t\n-+----------------------------------------------------------------------------" << endl;

    int a,b;
    for (a=1;a<=9;a++) {
        cout << a << "|  ";
        for (b=1;b<=9;b++)
            cout << a*b << "\t";
        cout << endl;
    }
    system("pause");
    return 0;
}
