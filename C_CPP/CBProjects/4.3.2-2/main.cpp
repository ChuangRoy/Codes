#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    char letter;
    cout << "Input a charter:";
    cin >> letter;

    if (letter >= 'A' && letter <= 'Z')
        cout << letter << " is a capital letter" << endl;

    else
        cout << letter << " is not a capital letter" << endl;


    system("pause");
    return 0;
}
