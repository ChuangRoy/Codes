#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    char a;
    cout << " 輸入一個字元：";
    cin >> a;

    a = toupper(a);

    switch (a) {
        case 'A':cout << " 這是母音" << endl;break;
        case 'E':cout << " 這是母音" << endl;break;
        case 'I':cout << " 這是母音" << endl;break;
        case 'O':cout << " 這是母音" << endl;break;
        case 'U':cout << " 這是母音" << endl;break;
        default:cout << " 這不是母音" << endl;break;
    }

    return 0;
}
