#include <iostream>

using namespace std;

int main()
{
    long double x=0.0;
    for (int i=1;i<=1000;i++) {
        if (i%2==1)
            x += 4.0/(2*i-1);
        if (i%2==0)
            x -= 4.0/(2*i-1);
        // cout << x << endl;
    }
    cout << x << endl;
    return 0;
}
