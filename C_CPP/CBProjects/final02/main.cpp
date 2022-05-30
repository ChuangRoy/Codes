#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int Chinese,English,Math;
    int total;
    float average;
    cout << " 請輸入國、英、數 三科成績：";
    cin >> Chinese >> English >> Math;
    cout << " DEBUG: " << " Chinese: " << Chinese <<
            "   English:" << English << "   Math:" << Math << endl;

    total = Chinese + English + Math;
    average = total /3.0;
    cout << " DEBUG: " << "Average = " << average << " (Average*100) = " << (int(average*100)+1)
            << " (Average*100)%10 = " << (int(average*100)+1)%10 << endl;
    if ((int(average*100)%10) >= 5) // 四捨五入到小數一位
        average = int(average*10)/10.0+0.1;
    else
        average = int(average*10)/10.0;

    cout << " DEBUG: " << " Total = " << total << endl;
    cout << " DEBUG: " << " Average = " << average << endl;

    cout << endl;
    cout << " 國文\t英文\t數學\t總分\t平均" << endl;
    cout << " " << Chinese << "\t" << English << "\t"
            << Math << "\t" << total << "\t" << average << "\t";
    return 0;
}
