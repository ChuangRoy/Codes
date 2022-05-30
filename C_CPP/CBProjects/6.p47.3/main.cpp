#include <iostream>

using namespace std;

int main()
{
    int n, i, a[1000], maxI = 0;
    cout << " 請輸入數字：";
    cin >> n;
    if (n > 1000)
        n = 1000;
    for (i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (i = 0; i < n; i++) {
        if (a[i] >  a[maxI])
            maxI = i;
    }
    cout << " 最大值是：" << a[maxI] << endl;
    cout << " 最大值是第 " << maxI+1 << " 個數字" << endl;

    return 0;
}
