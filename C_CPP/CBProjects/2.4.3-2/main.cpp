#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    double Fahrenheit; // Fahrenheit：華氏
    cout << " 請輸入華氏度數： ";
    cin >> Fahrenheit;

    cout << " 攝氏度數為：" << fixed << setprecision(3)  << // fixed << setprecision(位數) 取四捨五入到__位
        (Fahrenheit - 32) * 5 / 9 << endl;
    return 0;
}
