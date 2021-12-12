#include <iostream>
#include <graphics.h>
#include <math.h>
using namespace std;

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);
	int angle = 0;
	double x, y;
	
    for (x = 0; x <1500; x += 5)
    {
        y = 50 * sin(x * 3.141 / 180);
        setcolor(WHITE);
        setfillstyle(SOLID_FILL,WHITE);
        circle(100+x,240+y,20);
        line(0+x,170,200+x,170);
        line(0+x,310,200+x,310);
        floodfill(100+x,240+y,WHITE);
        delay(50);
        cleardevice();
    }
    
    getch();
    closegraph();
    return 0;
}
