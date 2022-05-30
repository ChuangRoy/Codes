#include <iostream>
#include <ctime>
#include <cstdlib>
#include <stdlib.h>

using namespace std;

int main()
{
    int i = 0,number,ans;

    while(1)
    {
            srand(time(0));
            ans=1+rand()%101;
    while (1)
    {
        cout << " 請輸入一個整數:";
        cin >> number;
        if (number>=1&&number<=100)
        {
            i++;
            system("cls");
            if (number==ans)
            {
                system("color 10");
                cout<<" 你猜對了"<<endl;
                break;
            }
            else if (number<ans)
            {
                system("color 04");
                cout<<" 數值太小"<<endl;
            }
            else
            {
                system("color 04");
                cout<<" 數值太大"<<endl;
            }
            cout <<" 你共猜了"<<i<<" 次"<<endl;

        }
        else
            cout<<" 請輸入1~100的數"<<endl;

        }
        cout << " 遊戲重新開始" << endl;
        i = 0;

    }


    return 0;
}
