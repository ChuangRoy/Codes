#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{

    int l=1,r=101,n,i=0;
    char a;

    while (1)
    {
        i++;
        n=(l+r)/2;
        cout << n << endl;
        cin >> a;

        if (a=='c')
        {
            cout << " 我猜對了!" << endl;
            break;
        }
        else if (a=='b')
            r=n;
        else if (a=='s')
            l=n;

        system("cls");
        cout << " 我猜了 " << i << " 次" << endl;
    }


    return 0;
}
