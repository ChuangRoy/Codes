#include <iostream>

using namespace std;

int main()
{
    int a[6];
    int sum = 0;
    int i , j , k;
    int minI;
    for (i = 0 ; i < 6 ; i++) {
        cout << " 輸入 " << i+1 << " 號成績 ： ";
        cin >> a[i];
        sum += a[i];
    }
    int b[] = {1 , 2 , 3 , 4 , 5 , 6};
    // selection sort

    for (j = 0 ; j < 6 ; j++) {
        minI = j;
        for (k = j ; k < 6 ; k++) {
            if (a[minI] > a[k])
                minI = k;
        }
        int temp = a[j];
        a[j] = a[minI];
        a[minI] = temp;
        temp = b[j];
        b[j] = b[minI];
        b[minI] = temp;
    }

    cout << endl << endl;
    for (int _i = 1 ; _i <= 6 ; _i++) {
        if (a[6-_i] == a[6-_i])
        cout << " 第 " << _i << " 名 ： " << b[6-_i] << " 號 " << a[6-_i] << " 分" << endl;

    }
    cout << endl << endl;
    cout << " 總成績為 " << sum << endl;
    cout << " 平均為 " << (float) sum / 6 << endl;

}
