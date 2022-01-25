#include <iostream>

using namespace std;

int A , B;

// 含式
int A_B(int $x,int Y1 , int $y2 , int $y3 , int $y4) {
    if ($x == Y1) {
        A ++;
    }else if ($x == $y2 || $x == $y3 || $x == $y4) {
        B ++;
    }

}

int main() {
    // 定義
    int x , y;
    int x1 , x2 , x3 , x4;
    int y1 , y2 , y3 , y4;
    A = 0, B = 0;
    // 輸入數字
    cout << " 輸入兩個數字：";
    cin >> x >> y;
    // 取 X 位數
    x4 = x % 10;
    x3 = x / 10 % 10;
    x2 = x / 100 % 10;
    x1 = x / 1000 % 10;
    // 取 Y 位數
    y4 = y % 10;
    y3 = y / 10 % 10;
    y2 = y / 100 % 10;
    y1 = y / 1000 % 10;

    cout << " x:" << x1 << x2 << x3 << x4 << endl;
    cout << " y:" << y1 << y2 << y3 << y4 << endl;

    // 窮舉
    A_B(x1,y1,y2,y3,y4);
    A_B(x2,y2,y1,y3,y4);
    A_B(x3,y3,y1,y2,y4);
    A_B(x4,y4,y1,y2,y3);

    cout << " A:" << A << " B:" << B;

    return 0;
}
