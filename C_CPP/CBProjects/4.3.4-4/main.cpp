#include <iostream>
#include <stdlib.h>

using namespace std;

// 閏年判斷，return 1 或 0
int leap_year(int $year){
    return (($year % 400 == 0) || (($year % 100 != 0) && ($year % 4 == 0)));
}

int main()
{
    int total_days_this_year = 0,total_days = 0; // Define
    float year,month,day; // Define 避免惡搞
    string Week_Day; // 星期幾
    cout << "Input year month day:";
    cin >> year >> month >> day;
    total_days = 365*(year-1) + (year-1)/4 - (year-1)/100 + (year-1)/400; //從現在到前一年的12月31日有幾天

    if (year-int(year)!=0 || month-int(month)!=0 || day-int(day)!=0){ //避免惡搞：輸入小數判斷
        cout << "Input Error !" << endl;
        system("pause");
        return 0;
    }
    //避免惡搞：輸入日期判斷
    if (year <= 0 || month < 1 || month > 12 || (month==2 && day > 28+(leap_year(year))) || ((month == 4 || month == 6 || month == 9 || month == 11) && day > 30) || day > 31){
        cout << "Input Error !" << endl;
        system("pause");
        return 0;
    }
    // 今年天數總和
    int a[] = {31,28+leap_year(year),31,30,31,30,31,31,30,31,30,31};
    for (int i = 0;i <= month-2;i++){ // month -2 :第一項是a[0] -1  前一個月 -1
        total_days_this_year += a[i];
    }
    total_days_this_year += day;
    total_days += total_days_this_year;
    cout << year << "." << month << "." << day << " is the "<< total_days_this_year << "th day of this year" << endl;
    cout << "Total day is " << total_days << " days" << endl << endl;

    // 星期幾判斷
    switch((total_days+1)%7){
        case 1:Week_Day = "Monday";break;
        case 2:Week_Day = "Tuesday";break;
        case 3:Week_Day = "Wednesday";break;
        case 4:Week_Day = "Thursday";break;
        case 5:Week_Day = "Friday";break;
        case 6:Week_Day = "Saturday";break;
        case 0:Week_Day = "Sunday";break;
    }
    cout << "This day is " << Week_Day << endl;
    system("pause");
    return 0;
}
