#include <iostream>

using namespace std;

int main()
{
    int n1,n2;
    cin >> n1 >> n2;
    cout << endl << "  " << n1 << endl;
    cout << "X" << "  " << n2 << endl;
    cout << "-----------" << endl;
    cout << "  " << n1 * (n2 % 10) << endl;
    cout << " " << n1 * (n2 / 10 % 10) << " " << endl;
    cout << "-----------" << endl;
    cout << " " << n1 * n2 << endl;
    return 0;
}
