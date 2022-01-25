#include <iostream>

using namespace std;

// 宣告類別
class Demo {
// 宣告 public 成員
public:
    int a;
    int b;
    int DoSomething();
};

// 實作 Demo 的 DoSomething() 成員函數
int Demo::DoSomething() {
    return a + b;
}

// 程式執行的 main()
int main(void) {
    // 宣告並建立 Demo 型態的物件 t
    Demo t;
    t.a = 11; // 直接設定成員變數值
    t.b = 22;
    cout << endl;
    // 呼叫並印出 DoSomething() 的回傳值
    cout << t.DoSomething() << endl;
    cout << endl;

    return 0;
}

/* 《程式語言教學誌》的範例程式
   http://kaiching.org/
   檔名：class_demo.cpp
   功能：示範定義類別
   作者：張凱慶 */
