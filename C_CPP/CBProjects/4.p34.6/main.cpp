#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    float km;
    int $;
    cout << " 輸入里程數(km)：";
    cin >> km;
    if (km <= 1)
       $ = 65;
    else {
        $ = 65;
        $ += (int(km-1)/500+1)*5;
    }
    cout << " 你需要付 " << $ << " 元" << endl;
    system("pause");
    return 0;
}
