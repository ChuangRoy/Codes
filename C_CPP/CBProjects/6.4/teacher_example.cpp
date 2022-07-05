#include <iostream>

using namespace std;

int main()
{
    int c,r,maxr,temp;
    //                    00 01 02 03 04 05
    int score[6][6] = {  {86,92,57,81,65,0},
                         {96,98,81,67,74,0},
                         {91,73,92,78,67,0},
                         {68,88,90,89,78,0},
                         {87,96,70,62,68,0},
                         {84,75,94,80,90,0}};
    //求總分
    for (r = 0; r < 6; r++)
    {
        for (c = 0; c < 5; c++)
        {
            score[r][5] += score[r][c];
        }
    }
    //依總分排序
    maxr=0; //第一
    for(r=1;r<6;r++)
        if(score[r][5]>score[maxr][5])
            maxr=r;
    temp=score[0][0];
    score[0][0]=score[maxr][0];
    score[maxr][0]=temp;
    //
    temp=score[0][1];
    score[0][1]=score[maxr][1];
    score[maxr][1]=temp;
    //
    temp=score[0][2];
    score[0][2]=score[maxr][2];
    score[maxr][2]=temp;
    //
    temp=score[0][3];
    score[0][3]=score[maxr][3];
    score[maxr][3]=temp;
    //
    temp=score[0][4];
    score[0][4]=score[maxr][4];
    score[maxr][4]=temp;

    maxr=1;  //第二
    for(r=2;r<6;r++)
        if(score[r][5]>score[maxr][5])
            maxr=r;





    //輸出


    return 0;
}