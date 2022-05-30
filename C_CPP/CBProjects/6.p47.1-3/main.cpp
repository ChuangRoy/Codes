#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main()
{
    int a;
    srand(time(NULL));
    a = rand() % 3;

    cout << a-2 << endl;

    return 0;
}
