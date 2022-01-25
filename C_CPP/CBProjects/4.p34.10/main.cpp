#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    float m,kg,bmi;
    string result;
    cout << " 請輸入身高(cm)；";
    cin >> m;
    m /= 100;
    cout << " 請輸入體重(kg)：";
    cin >> kg;

    bmi = kg/(m*m);

    cout << " 你的身高(m)：" << m << " 你的體重(kg)：" << kg << " 你的BMI：" << bmi << endl;

    if (bmi < 18.5)
      result = "過輕";
    else if (bmi >= 18.5 && bmi < 24)
      result = "正常範圍";
    else if (bmi >= 24 && bmi < 27)
      result = "過重";
    else if (bmi >= 27 && bmi < 30)
      result = "輕度肥胖";
    else if (bmi >= 30 && bmi < 35)
      result = "中度肥胖";
    else if (bmi >= 35)
      result = "重度肥胖";
    else {
      cout << " 輸入錯誤！";
      system("pause");
      return 1;
    }

    cout << " 計算結果是 " << result << endl;
    system("pause");
    return 0;
}
