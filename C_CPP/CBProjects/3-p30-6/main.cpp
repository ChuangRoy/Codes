#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int a,digits,odd_total,even_total;
    digits = 0;
    odd_total = 0,even_total = 0;
    cout << "Input a integer:";
    cin >> a;
    while (a != 0) {
        if(digits==0){
            odd_total += a % 10;

        }else if(digits%2==1){
            even_total += a % 10;

        }else{
            odd_total += a % 10;

        }
        digits += 1;
        a /= 10;
    }
    cout << "odd number totals:" << odd_total << endl;
    cout << "even number totals:" << even_total << endl;
    system("pause");
    return 0;
}
