#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    int a[8], i, key, loc[8] = {0} , log = 0;
    srand(time(NULL));
//////////產生亂數////////
    for (i = 0; i < 8; i++) {
        a[i] = rand() % 11 + 20;
        cout << "a[" << i << "] = " << a[i] << "\t";
    }

    cout << endl;

/////////輸入////////////
    cout << " 輸入欲搜尋的整數：";
    cin >> key;

///////搜尋///////////
    for (i = 0; i < 8; i++) {
        if (a[i] == key) {
            cout << "a[ " << i << " ] = " << key << endl;
            log++;
        }
    }

    if (log != 0) {
    }
    else
        cout << " 沒搜尋到" << key << endl;

    return 0;
}
