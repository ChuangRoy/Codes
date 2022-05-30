#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

int main()
{
    // 定義變數
    int Chinese,English,Math,Sum;
    float Average;
    // 輸入
    cout << " 請輸入國文、英文、數學三科成績：";
    cin >> Chinese >> English >> Math;
    // 處理
    Sum = Chinese+English+Math;
    Average = Sum/3.000;
    // 輸出
    cout << " 國文\t英文\t數學\t總分\t平均\t是否及格" << endl;
    cout << " " << Chinese << "\t" << English << "\t" << Math << "\t" << Sum << "\t" << fixed << setprecision(1) << Average;
    (Average >= 60)?cout << "\t" << " 是":cout << "\t" << " 否"; // 及格判斷
    // Exit
    cout << endl << endl; // 空行
    system("pause");
    return 0;
}
