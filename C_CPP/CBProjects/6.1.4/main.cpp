#include <iostream>

using namespace std;

int main()
{
    // int n = 8;
    int a[] = {7, 8, 4, 1, 3, 5, 9, 2};
    int b[] = {-2, 0, 5, -1, 3, 8, -8, 9};
    int c[8], i, temp;
    int d[16];
    int j , k;
    int minI;

    for (i = 0 ; i < 8 ; i++)
        c[i] = a[i] + b[i];

    cout << "a + b = ";
    for (i = 0 ; i < 8 ; i++)
        cout << c[i] << " ";
    cout << endl;


    for (i = 0 ; i < 8 ; i++)
        d[i] = a[i];

    for (i = 0 ; i < 8 ; i++)
        d[i+8] = b[i];

// int j , k , minI;
    for (j = 0 ; j < 16 ; j++) {
        minI = j;
        for (k = j ; k < 16 ; k++) {
            if (d[minI] > d[k])
                minI = k;
        }
        temp = d[j];
        d[j] = d[minI];
        d[minI] = temp;
    }

    for (i = 0 ; i < 16 ; i++)
        cout << d[i] << " ";

    cout << endl;
    return 0;
}
