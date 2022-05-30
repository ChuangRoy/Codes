#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int a,b,sum=0;

    cout << " 輸入兩個整數：";
    cin >> a >> b;

    int i;
    for(i=a;i<=b;i++) {
        if ((i%2)==0) {
            cout << " 偶數：" << i << endl;
            sum += i;
        }

    }

    cout << " 偶數和 = " << sum << endl;
    system("pause");
    return 0;
}
