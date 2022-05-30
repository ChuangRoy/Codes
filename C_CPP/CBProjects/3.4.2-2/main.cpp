#include <iostream>
using namespace std;
int main()
{
	int h, w;
	double bmi, m;
	cout << "Input height cm :";
	cin >> h;
	cout << "Input weight kg :";
	cin >> w;
	m = (double) h / 100;
	bmi = w /(m * m);
	cout << "BMI : " << bmi << endl;
	return 0;
}
