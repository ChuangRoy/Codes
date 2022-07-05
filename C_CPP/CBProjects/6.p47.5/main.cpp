#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int i, n[100], a, Is_Jolly_Jumper = 1;
    cout << "請輸入一串數字：";
    cin >> a;
    if (a > 100) {
        a = 100;
    }
    for (i = 0; i < a; i++) {
        cin >> n[i];
    }
    int l[a-1];
    for (i = 1; i < a; i++) {
        l[i-1] = i;
    }
    for (i = 1; i < a; i++) {
        if (abs(n[i] - n[i-1]) == l[i-1])
            continue;
        else {
            Is_Jolly_Jumper = 0;
            break;
        }
    }
    if (Is_Jolly_Jumper)
        cout << "These are jolly jumper" << endl;
    else
        cout << "These are not jolly jumper" << endl;
    return 0;
}
