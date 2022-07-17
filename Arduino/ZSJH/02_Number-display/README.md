# 獨立研究04 Arduino
###### tags: `獨立研究`

[TOC]

## 七段顯示器
### 七段顯示器元件的位置
![七段顯示器元件的位置](https://i.imgur.com/1jFMy46.png)

### 腳位對照表
|1|2|3|
|----|----|----|
||A||
|F||B|
||G||
|E||C|
||D|dp|

![腳位對照表](http://lh6.ggpht.com/_Ap9EEd9K-fg/TRS22TOUYLI/AAAAAAAADMQ/thewstv3f38/image_thumb%5B5%5D.png?imgmax=800)

### 數字對照表
|數字|LED(a~g)|
|----|-----|
|0|1,1,1,1,1,1,0|
|1|0,1,1,0,0,0,0|
|2|1,1,0,1,1,0,1|
|3|1,1,1,1,0,0,1|
|4|0,1,1,0,0,1,1|
|5|1,0,1,1,0,1,1|
|6|1,0,1,1,1,1,1|
|7|1,1,1,0,0,0,0|
|8|1,1,1,1,1,1,1|
|9|1,1,1,1,0,1,1|

### Code

```cpp=
// C++ code
// Made by tinkercad

byte led_numbers [10] [7] = {
  {1,1,1,1,1,1,0}, // 0
  {0,1,1,0,0,0,0}, // 1
  {1,1,0,1,1,0,1}, // 2
  {1,1,1,1,0,0,1}, // 3
  {0,1,1,0,0,1,1}, // 4
  {1,0,1,1,0,1,1}, // 5
  {1,0,1,1,1,1,1}, // 6
  {1,1,1,0,0,0,0}, // 7
  {1,1,1,1,1,1,1}, // 8
  {1,1,1,1,0,1,1}, // 9
  };
void setup()
{
  for (int i=2 ; i <= 8 ; i++) {
    pinMode(i,OUTPUT);
  }

}

void loop()
{
  for (int j = 0 ; j <= 9 ; j++) {
    for (int k = 0 ; k < 7 ; k++) {
   	  digitalWrite(k+2,led_numbers[j][k]);
    }
    delay (1000);
  }
}
```
### 成品
![成品圖](https://i.imgur.com/CPBpy1R.png)

