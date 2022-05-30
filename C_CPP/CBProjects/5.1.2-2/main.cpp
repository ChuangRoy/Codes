#include <iostream>
#include <stdlib.h>
#include <iomanip>

using namespace std;

int main()
{
    int i,j,k;
    // 1
    for (i=0;i<=5;i++) {
        for (j=0;j<=i;j++)
            cout << "*" ;
    cout << endl;
    }

    // 2
    cout << endl;
    for (i=0;i<=5;i++) {
        for (j=5;j>=i;j--)
            cout << "*" ;
    cout << endl;
    }

    // 3
    cout << endl;
    for (i=0;i<=5;i++) {
        for (k=0;k<=i;k++)
            cout << " " ;
        for (j=5;j>=i;j--)
            cout << "*" ;
        cout << endl;
    }

    // 4
    cout << endl;
    for (i=0;i<=5;i++) {
        for (k=5;k>=i;k--)
            cout << " " ;
        for (j=0;j<=i*2;j++)
            cout << "*" ;
        cout << endl;
    }

    system("pause");
    return 0;
}
