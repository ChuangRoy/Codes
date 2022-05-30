#include <iostream>

using namespace std;

int main()
{
    int n1 , n2 , temp;
    cout << " 請輸入兩個數：";
    while(cin >> n1 >> n2) {
        while(n1%n2) {
            temp = n1 % n2;
            n1 = n2;
            n2 = temp;
        }
        cout << " " << n1 << " 和 " << n2 << " 的最大公因數是 " << n2 << endl ;
        break;
    }

    return 0;
}
