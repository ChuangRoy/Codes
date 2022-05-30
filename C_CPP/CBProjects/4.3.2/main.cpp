#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int n;
    cout << " 請輸入數字n：";
    cin >> n;

    if (n%2)
        cout << "odd";
    else
        cout << "even";

    cout << endl;
    system("pause");
    return 0;
}
