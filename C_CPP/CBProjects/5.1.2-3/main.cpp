#include <iostream>

using namespace std;

int main()
{
    int a,b,c,n,total;
    cout << " 請輸入n：";
    cin >> n;
    total=0;
    for (a=0;a<=n;a++) {
        for (b=0;b<=n;b++) {
            for (c=0;c<=n;c++) {
                if ((a*a)+(b*b)==(c*c)) {
                    if (a<b && b<c) {
                        cout << " 找到 " << a << " "<< b << " " << c << endl;
                        total += 1;
                    }
                }
            }
        }
    }

    cout << " 共有 " << total << " 個";
    return 0;
}
