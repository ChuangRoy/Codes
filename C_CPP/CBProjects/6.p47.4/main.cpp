#include <iostream>

using namespace std;

int main()
{
    int a[1000], n = 0, i = 0, b, j;
    cout << " 請輸入一串數字：";
    while (cin >> a[i]) {
        i++;
    }
    cout << " 請輸入一個數字：";
    cin.clear();
    cin.ignore(100, '\n');
    cin >> b;
    for (j = 0; j < i; j++) {
        if (a[j] > b)
            n++;
    }
    cout << " 比 " << b << " 還要大的有 " << n << " 個數字" << endl;

    return 0;
}
