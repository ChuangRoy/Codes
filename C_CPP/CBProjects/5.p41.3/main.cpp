#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a;
    cout << "Choose a mode:";
    cin >> a;
    int n,x=0;
    cout << endl;
    cout << "Input a number:";
    cin >> n;
    if (a==1) {
        x = 1;
        for (int i=1;i<=n;i++)
            x *= i;
        cout << x << endl;
    }
    if (a==2) {
        for (int i=1;i<=n;i++) {
            if (i%2==1)
                x += i;
            else
                x -= i;
        }
        cout << x << endl;
    }
    if (a==3) {
        long double X=0;
        for (int i=1;i<=n;i++)
            X += 1.0/i;
        cout << X << endl;
    }
    if (a==4) {
        bool prime = 1;
        int root;
        for (int i=2;i<=n;i++) {
            if (n%i==0) {
                root = sqrt(i);
                for (int j=2;j<=root;j++) {
                    if (i%j==0) {
                        prime = 0;
                    }
                }
                if (prime) {
                    x += i;
                }
            }
        }
        cout << x << endl;
    }
    return 0;
}
