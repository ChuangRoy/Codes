#include <iostream>

using namespace std;

int main()
{
    int main_seconds,hours,minuts,seconds;
    cout << "Input seconds:";
    cin >> main_seconds;

    hours = main_seconds / 60 /60;
    minuts = main_seconds / 60 % 60;
    seconds = main_seconds % 60;

    cout << hours << " h " << minuts << " m " << seconds << " s ";
    return 0;
}
