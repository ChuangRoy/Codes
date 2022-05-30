#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main()
{
    int a[6] = {0} , i , j;
    srand(time(NULL));
    for (i = 0 ; i < 6 ; i++) {
        a[i] = (rand() % 6) + 1;
        for (j = 0 ; i < i ; j++) {
            if (a[i]==a[j]) {
                i--;
                a[i] = 0;
            }
        }
    }
    for (i = 0 ; i < 6 ; i++)
        cout << "a[" << i << "] = " << a[i] << "\t";

    return 0;
}
