#include <iostream>

using namespace std;

int main()
{
    int number;
    cout << "Input student numbers:";
    cin >> number;
    (number%3==0)?cout << "Team " << number/3:cout << "Team " << number/3 + 1;
    return 0;
}
