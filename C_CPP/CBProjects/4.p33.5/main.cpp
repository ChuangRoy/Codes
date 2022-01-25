#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{

    float h ,m;
    cout << " 請輸入小時 分鐘：";
    cin >> h >> m;
    string message;

    if ( (h>24||h<0) || (m>60||m<0) || !(h-int(h)==0) || !(h-int(h)==0) ) {
        cout << " 輸入錯誤" << endl;
        system("pause");
        return 1;
    }

    if (h==7||h==8||h==9||h==10||h==11||h==12||h==13||h==14||h==15||h==16) {
    // if (h==7...16) {
        if((h==7&&m<50)||(h==16&&m>30)) {
            message = " 不是上課時間";
        }else{
            message = " 上課時間";
        }
    }

    cout << message << endl;
    system("pause");
    return 0;

}
