#include <iostream>

using namespace std;

int main()
{
    int n , a[100] = {0} , i=0 , j;
    cout << "Input n：";
    cin >> n;

    while (n > 0) {
        a[i] = n %2;
        n = n / 2;
        i++;
    }
    for (j = i -1 ; j >=0 ; j--)
        cout << a[j];
    cout << endl;

    return 0;
}
