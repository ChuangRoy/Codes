#include <iostream>

using namespace std;

int main()
{
    int n;

    cout << " 輸入西元年 (大於1911) :";
    cin >> n;
    while (n < 1911) {
       cout << " 請勿惡作劇" << endl;
       cout << " 輸入西元年 (大於1911) :";
       cin >> n;
    }

//    if (n <= 1911) {
//        cout << " 請勿惡作劇" << endl;
//        cout << " 輸入西元年";
//        cin >> n;
//    }

    cout << " 民國 " << n - 1911 << " 年" << endl;
    return 0;
}
