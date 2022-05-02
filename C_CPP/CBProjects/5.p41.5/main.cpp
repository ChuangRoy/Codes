#include <iostream>

using namespace std;

int main()
{
    int sum;
    int a,b,c,d;
    int count_ = 0;
    for (int i = 1 ; i <= 10000 ; i++) {
        a = i%10;
        b = i/10 %10;
        c = i/100 %10;
        d = i/1000 %10;
        sum = a + b + c + d;
        if (sum==9) {
            cout << d << c << b << a << endl;
            count_++;
        }
    }
    cout << endl << count_;
    return 0;
}
