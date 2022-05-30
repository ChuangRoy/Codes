#include <iostream>

using namespace std;

int main()
{
    int n , i=0;
    int a[256]  , b[256] , temp;
    cout << "Input (ctrl+z for stop):";
    while (cin >> a[i]) {
        if (i == 256)
            break;
        i++;
    }
    n = i;
    for (i = 0 ; i < n ; i++) {
        b[n-i-1] = a[i];
    }
    cout << "Output:";
    for (i = 0 ; i < n ; i++)
        cout << b[i] << " ";
}

