#include <iostream>
#include <stdlib.h>

using namespace std;

int leap_year(int $year){
    return (($year % 400 == 0) || (($year % 100 != 0) && ($year % 4 == 0)));
}

int main()
{
    int year,month,day;
    int days = 0;
    cout << "Input year month day:";
    cin >> year >> month >> day;
    int a[] = {31,28+leap_year(year),31,30,31,30,31,31,30,31,30,31};
    for (int i = 0;i <= month-2;i++){
        days += a[i];
    }
    days += day;
    cout << days << endl;
    system("pause");
    return 0;
}
