#include <iostream>

using namespace std;

int main()
{
    float feet;
    float inches;

    cout << " 請輸入英尺：";
    cin >> feet;
//    cout << " " << feet << " 英尺 = " << feet * 12 * 2.54 << " 公分";

    cout << endl << " 請輸入英吋：";
    cin >> inches;
//    cout << " " << inches << " 英尺 = " << inches * 2.54 << " 公分";

    cout << " "  << feet << " 英尺和 " << inches << " 英吋 = " << (feet * 12 * 2.54) + (inches * 2.54) << " 公分";

    return 0;
}
