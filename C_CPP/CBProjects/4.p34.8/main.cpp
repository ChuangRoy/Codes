#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    char letter;
    string message;

    cout << " 輸入一個字母：";
    cin >> letter;

    switch(letter) {
        case 'A'...'Z':message = " 大寫";break;
        case 'a'...'z':message = " 小寫";break;
        default:message = " 特殊字元";break;

    }

    cout << message << endl;
    system("pause");
    return 0;
}
