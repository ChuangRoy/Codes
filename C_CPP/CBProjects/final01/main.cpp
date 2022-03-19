#include <iostream>

using namespace std;

int main()
{
    float S; // distance
    int $;
    cout << " 請輸入距離(km):";
    cin >> S;
    cout << " DEBUG: " << S << " km" << endl;
    if (S<1) {
        $ = 65;
        cout << " DEBUG: " << S << " km < 1 km    $65" << endl;
    }
    else {
        $=65;
        cout << " DEBUG: " << S << " km >= 1 km" << endl;
        if ((((S-1)/0.5-int((S-1)/0.5))==0)) {// distance/0.5 km = 0 ?
            $ += ((S-1)/0.5)*5;
            cout << " DEBUG: " << S-1 << "/0.5 is integer:(S-1)/0.5" << endl;
        }
        else {
            $ += (int((S-1)/0.5)+1)*5;
            cout << " DEBUG: " << S-1 << "/0.5 is not integer:int((S-1)/0.5)+1" << endl;
        }
    }
    cout << " 你需要付 " << $ << " 元" << endl;

    return 0;
}
