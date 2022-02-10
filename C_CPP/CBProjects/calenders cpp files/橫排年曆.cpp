#include <iostream>
#include <iomanip>
#include <stdlib.h>

using namespace std;

// 閏年判斷，return 1 或 0
int leap_year(int $year){
    return (($year % 400 == 0) || (($year % 100 != 0) && ($year % 4 == 0)));
}

string get_month_text(int $month) {
    string month_text;
    switch(int($month)) {
        case 1:month_text = "Jan";break;
        case 2:month_text = "Feb";break;
        case 3:month_text = "Mar";break;
        case 4:month_text = "Apr";break;
        case 5:month_text = "May";break;
        case 6:month_text = "Jun";break;
        case 7:month_text = "Jul";break;
        case 8:month_text = "Aug";break;
        case 9:month_text = "Sep";break;
        case 10:month_text = "Oct";break;
        case 11:month_text = "Nov";break;
        case 12:month_text = "Dec";break;
      }
    return month_text;
}


int main()
{
    int total_days_this_year = 0; // Define
    int total_days_1,total_days_2,total_days_3;
    float year; // Define 避免惡搞
    int month;
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

    for (month=1;month<=12;month+=3) {  // 一次跳三個月份
        total_days_1 = 365*(year-1) + (year-1)/4 - (year-1)/100 + (year-1)/400; //從現在到前一年的12月31日有幾天

        cout << "        " << "--" << int(year) << "." << get_month_text(month) << "--    ";
        cout << "                  " << "--" << int(year) << "." << get_month_text(month+1) << "--    ";
        cout << "                  " << "--" << int(year) << "." << get_month_text(month+2) << "--    " << endl;
        cout << " Sun Mon Tue Wed Thu Fri Sat     " << " Sun Mon Tue Wed Thu Fri Sat     " << " Sun Mon Tue Wed Thu Fri Sat" << endl;
        cout << "=============================    "  << "=============================    " << "=============================    " << endl;
        total_days_this_year = 0;
        int a[] = {0,31,28+leap_year(year),31,30,31,30,31,31,30,31,30,31};  // 每月天數
        for (int i = 0;i <= month-1;i++){ // month -1 :前一個月
            total_days_this_year += a[i];
        }
        total_days_this_year += 1;
        total_days_1 += total_days_this_year;
        total_days_2 = total_days_1 += a[month+1];
        total_days_3 = total_days_2 += a[month+2];


        int days_count[13]={0,1,1,1,1,1,1,1,1,1,1,1,1};
        for (int i=1;i<=6;i++) {  // 六行
            for (int j=1;j<=7;j++) { // 第一個月
              if (days_count[month]<=(total_days_1%7))
                 cout << "    ";
              else if((days_count[month]-(total_days_1%7))>a[month])
                cout << "    ";
              else
                cout << setw(4) << (days_count[month]-(total_days_1%7));
              days_count[month]=days_count[month]+1;
            }
            cout << "    ";

            for (int j=1;j<=7;j++) { // 第二個月
              if (days_count[month+1]<=(total_days_2%7))
                 cout << "    ";
              else if((days_count[month+1]-(total_days_2%7))>a[month+1])
                cout << "    ";
              else
                cout << setw(4) << (days_count[month+1]-(total_days_2%7));
              days_count[month+1]=days_count[month+1]+1;
            }
            cout << "    ";

            for (int j=1;j<=7;j++) { // 第三個月
              if (days_count[month+2]<=(total_days_3%7))
                 cout << "    ";
              else if((days_count[month+2]-(total_days_3%7))>a[month+2])
                cout << "    ";
              else
                cout << setw(4) << (days_count[month+2]-(total_days_3%7));
              days_count[month+2]=days_count[month+2]+1;
            }
          cout << endl;
        }
        cout << endl << endl;
    }

    cout << endl;
    system("pause");
    return 0;
}

