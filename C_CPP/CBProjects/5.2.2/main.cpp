#include <iostream>
#include <climits>

using namespace std;

int main()
{
    int n, count = 1, sum = 0;
    int Max = INT_MIN, Min = INT_MAX;
    // cout << Max << endl << Min;

    do {
        cin >> n;
        Max = (Max < n)?n:Max;
        Min = (Min > n)?n:Min;
        sum += n;
        count++;
    }while(count <= 5);

    cout << "Max:" << Max << " Min:" << Min << " Average:" << sum / 5.0;



    return 0;
}
