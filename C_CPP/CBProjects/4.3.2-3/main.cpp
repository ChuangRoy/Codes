#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int money;
    cout << "Input money:";
    cin >> money;

    cout << "You need to pay:";
    (money >= 2000)?cout << int(money*0.9):cout << int(money*0.95);
    cout << endl;

    system("pause");
    return 0;
}
