#include <iostream>

using namespace std;

int main()
{
    string str = "This is a C++ program.";
    cout << "This is a \nC++ program." << endl << endl;
    for (int i = 0;i < int(str.size());i++) {
        cout << str.at(i) << endl;
    }
}
