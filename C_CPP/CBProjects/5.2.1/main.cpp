#include <iostream>

using namespace std;

int main()
{
    int n;
    int m;
    cout << " 請輸入一個整數：";
    cin >> n;

    while (n) {
        cout << n % 10;
        n /= 10;
    }

    return 0;
}
