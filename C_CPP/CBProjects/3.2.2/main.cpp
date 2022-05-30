#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int time;
    cout << "Input the TW time:";
    cin >> time;

    cout << "There is " << (time+24-15)%24 << " in US";


    return 0;
}
