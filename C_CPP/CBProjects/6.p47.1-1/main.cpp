#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main()
{
    int a;
    srand(time(NULL));
    a = rand() % 10;

    cout << a << endl;

    return 0;
}
