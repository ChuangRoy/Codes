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
    float year,month; // Define 避免惡搞
    string Week_Day; // 星期幾
    cout << "Input year:";
    cin >> year;


    if (year-int(year)!=0 ){ //避免惡搞：輸入小數判斷
        cout << "Input Error !" << endl;
        system("pause");
        return 0;
    }

    //避免惡搞：輸入日期判斷
    if (year <= 0){
        cout << "Input Error !" << endl;
        system("pause");
        return 0;
    }


for (month=1;month<=12;month++) {
    total_days = 365*int(year-1) + int(year-1)/4 - int(year-1)/100 + int(year-1)/400; //從現在到前一年的12月31日有幾天
    total_days_this_year = 0;
    // 今年天數總和
    int a[] = {0,31,28+leap_year(year),31,30,31,30,31,31,30,31,30,31};
    for (int i = 0;i <= month-1;i++){ // month -2 :第一項是a[0] -1  前一個月 -1
        total_days_this_year += a[i];
    }
    total_days_this_year += 1;
    total_days += total_days_this_year;
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
      cout << endl << endl;
  }

    cout << endl;
    system("pause");
    return 0;
}

