#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int i,j;
    for (i=0;i<5;i++) {
        for (j=0;j<10;j++)
            cout << "*";
        cout << endl;
    }
    system("pause");
    return 0;
}
