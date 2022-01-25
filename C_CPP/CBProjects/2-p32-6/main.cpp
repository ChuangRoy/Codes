#include <iostream>

using namespace std;

int main()
{
    int clothes;
    cout << " 請輸入今天賣了幾件衣服：";
    cin >> clothes;

    cout << endl << " 今天賺了 " << (clothes * 77) - 800 << " 元" ;
    return 0;
}
