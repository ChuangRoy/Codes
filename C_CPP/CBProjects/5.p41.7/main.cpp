#include <iostream>

using namespace std;

int main()
{
    int a;
    for (int x = 1 ; x <= 30000 ; x++) {
        a = 0;
        for (int i = 1 ; i < x ; i++) {
            if (x%i==0)
                a += i;
            if (x == a) {
                cout << x << endl;
                break;
            }
        }

    }
    return 0;
}
