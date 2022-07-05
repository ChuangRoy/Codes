#include <iostream>
using namespace std;

int main () {
    int n = 6, a[n] = {0, 2, 4, 6, 8, 10, 12, 14};
    int temp, i, j, k;
    for (k = 0; k < n - 2; k++)
    for (i = 1; i < n - k; i++) {
        if (a[i] > a[i + 1]) {
            temp = a[i];
            a[i] = a[i + 1];
            a[i + 1] = temp;
        }
    }
    for (j = 0; j < n; j++)
        cout << a[j] << "\t" << endl;

    return 0;
}

