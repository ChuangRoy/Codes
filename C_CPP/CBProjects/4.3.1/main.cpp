#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int score;
    cout << " 請輸入成績：";
    cin >> score;

    if (score >= 60)
        cout << " 恭喜過關" << endl;

    if (score < 60 && score >= 50)
        cout << " 再努力一下" << endl;
    if (score < 50)
        cout << " 廢物" << endl;

    system("pause");

    return 0;
}
