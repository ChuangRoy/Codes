#include <iostream>

using namespace std;

int main()
{
    int n=18;
    while (!((n%7==5)&&(n%11==5)&&(n%17==5)))
        n += 1;
    while(n<=5000) {
        cout << n << endl;
        n += 7*11*17;
    }
    return 0;
}
