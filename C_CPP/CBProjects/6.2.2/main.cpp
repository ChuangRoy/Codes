#include <iostream>
#include <cstring>
#include <string.h>

using namespace std;

int main()
{
    int n , i;
    char a[256] , temp;
    cout << "Input:";
    cin.getline(a , 1000);
    n = strlen(a);
    for (i = 0 ; i < n/2 ; i++) {
        temp = a[i];
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = temp;
    }
    cout << "Output:";
    for (i = 0 ; i < n ; i++)
        cout << a[i];

    return 0;
}
