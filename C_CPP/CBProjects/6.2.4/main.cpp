#include <iostream>
using namespace std;

int main () {
    int n = 8, a[n]={0, 2, 4, 6, 8, 10, 12, 14};
    int low = 0, high = n - 1, mid;
    int key = 8;
    while (low <= high) {
        mid = (low + high) / 2;
        if (a[mid] == key) {
            cout << " 鍵值" << key << " 在索引" << mid;
            break;
        }
        else if (a[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    if (low > high)
        cout << " 找不到鍵值" << key;

    return 0;
}
