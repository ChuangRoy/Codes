#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    float $;
    cout << " 請輸入購物金額：";
    cin >> $;
    if ($>=10000){
        if ($>=50000){
            if ($>=100000){
                if ($>=150000)
                    $ *= 0.8;
                else
                    $ *= 0.85;
            }else
                $ *= 0.9;
        }else
            $ *= 0.95;

    }

    cout << " 你需要付 " << $ << " 元" << endl;
    system("pause");
    return 0;
}
