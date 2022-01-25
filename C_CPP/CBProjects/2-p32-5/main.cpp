#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int moneys_I_have;
    int how_much_is_it;

    cout << " 請輸入錢包裡有多少錢：";
    cin >> moneys_I_have;

    cout << endl << " 請輸入物品要多少錢：";
    cin >> how_much_is_it;

    cout << endl << " 你剩下 " << moneys_I_have - how_much_is_it << " 元" << endl << endl;
    system("pause");
    return 0;
}
