#include <iostream>
#include <iomanip>
#include <stdlib.h>

using namespace std;

// 閏年判斷，return 1 或 0
int leap_year(int $year){
    return (($year % 400 == 0) || (($year % 100 != 0) && ($year % 4 == 0)));
}

int main()
{
    int total_days_this_year = 0,total_days = 0,days_of_current_month; // Define
    string month_text;
    float year,month,day; // Define 避免惡搞
    string Week_Day; // 星期幾
    cout << "Input year & month:";
    cin >> year >> month;
    day = 1;
    total_days = 365*(year-1) + (year-1)/4 - (year-1)/100 + (year-1)/400; //從現在到前一年的12月31日有幾天

    if (year-int(year)!=0 || month-int(month)!=0){ //避免惡搞：輸入小數判斷
        cout << "Input Error !" << endl;
        system("pause");
        return 0;
    }

    //避免惡搞：輸入日期判斷
    if (year <= 0 || month < 1 || month > 12){
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

/*
    cout << year << "." << month << "." << day << " is the "<< total_days_this_year << "th day of this year" << endl;
    cout << "Total day is " << total_days << " days" << endl << endl;

    // 星期幾判斷
    switch(total_days%7){
        case 1:Week_Day = "Monday";break;
        case 2:Week_Day = "Tuesday";break;
        case 3:Week_Day = "Wednesday";break;
        case 4:Week_Day = "Thursday";break;
        case 5:Week_Day = "Friday";break;
        case 6:Week_Day = "Saturday";break;
        case 0:Week_Day = "Sunday";break;
    }
    cout << "This day is " << Week_Day << endl;
*/

    switch(int(month)) {
      case 1:days_of_current_month = 31;month_text = "Jan";break;
      case 2:days_of_current_month = 28+leap_year(year);month_text = "Feb";break;
      case 3:days_of_current_month = 31;month_text = "Mar";break;
      case 4:days_of_current_month = 30;month_text = "Apr";break;
      case 5:days_of_current_month = 31;month_text = "May";break;
      case 6:days_of_current_month = 30;month_text = "Jun";break;
      case 7:days_of_current_month = 31;month_text = "Jul";break;
      case 8:days_of_current_month = 31;month_text = "Aug";break;
      case 9:days_of_current_month = 30;month_text = "Sep";break;
      case 10:days_of_current_month = 31;month_text = "Oct";break;
      case 11:days_of_current_month = 30;month_text = "Nov";break;
      case 12:days_of_current_month = 31;month_text = "Dec";break;
  }

/*
    cout << "Days of current month is " << days_of_current_month << " days" << endl;
    cout << endl;
*/

    cout << "        " << "--" << int(year) << "." + month_text + "--" << endl;
    cout << " Sun Mon Tue Wed Thu Fri Sat" << endl;
    cout << "=============================" << endl;
    for (int i=1;i<=(days_of_current_month+(total_days%7));i++) {
      if (i<=(total_days%7)) {
        cout << "    ";
      }
      else {
        cout << setw(4) << (i-(total_days%7));
          if (i%7==0)
            cout << endl;
      }
    }

    cout << endl;
    system("pause");
    return 0;
}
