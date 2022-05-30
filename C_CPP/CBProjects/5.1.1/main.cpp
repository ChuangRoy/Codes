#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n,sum = 0;
    int i;
    cout << " 輸入一個n:";
    cin >> n;

    for(int i = 0;i<=n;i++)
        sum += i;

    cout << " 從 1 加到 n = " << sum << endl;
    system("pause");
    return 0;
}
