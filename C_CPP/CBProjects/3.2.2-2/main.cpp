#include <iostream>

using namespace std;

int main()
{
    int students;
    cout << "Input students:";
    cin >> students;

    cout << "You need to pay " << (students / 12) * 50 + (students % 12) * 5 << " dollars";

    return 0;
}
