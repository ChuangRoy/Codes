#include <iostream>

using namespace std;

// 等比數列和

int main()
{
    double n, total = 0;
    cin >> n;
    total = n;

    do  {
        n /= 2;
        total += n;
    }while(n >= 0.5); // 0.5條件
    cout << total;

    return 0;
}
