#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;
// using namespace cv2;
using namespace std;


int main() {
    String imgName = "C:\\Users\\s0415\\a.jpg";
    Mat img;
    img = imread(imgName, IMREAD_COLOR);
    if (img.empty()) {
        cout << "Could not open or find the image" << endl;
        return -1;
    }
    //namedWindow("display", WINDOW_AUTOSIZE);
    imshow("display", img);
//    waitKey(0);
    getchar();
    cout << "hi";
    destroyWindow("display");
    return 0;
}

