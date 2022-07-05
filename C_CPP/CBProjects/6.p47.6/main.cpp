#include <iostream>

using namespace std;

int main()
{
    int a;
    cout << "A:";
    cin >> a;
    int n[a];
    n[0] = 1;
    n[1] = 1;
    if (a == 0)
        cout << "NULL" << endl;
    else if (a == 1)
        cout << "1" << endl;
    else {
        for (int i = 2; i < a; i++)
            n[i] = n[i-2] + n[i-1];

        cout << n[a-1];
    }

    return 0;
}
