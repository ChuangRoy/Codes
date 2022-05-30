#include <iostream>

using namespace std;

int main()
{
    int n , i;
    cout << " 請輸入一個整數：";

    while (cin >> n) {
        for (i=1;i<=n;i++) {
            if ((n%i)==0)
                cout << " " << i << " 是 " << n << " 的因數" << endl;
        }
    }

    return 0;
}
