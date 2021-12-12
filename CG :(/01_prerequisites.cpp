#include<bits/stdc++.h>
#include<graphics.h>
using namespace std;
void snowman()
{
	int gd,gm;
	gd = DETECT;
	initgraph(&gd,&gm,NULL);
	int border_color = WHITE;
	setfillstyle(SOLID_FILL,WHITE);
	arc(300,350,0,360,70);
	floodfill(300,350,border_color);
	arc(300,232,0,360,50);
	floodfill(300,232,border_color);
	
	setcolor(BLACK);
	arc(275,225,0,360,8);
	floodfill(275,225,border_color);
	arc(325,225,0,360,8);
	floodfill(325,225,border_color);
	setcolor(LIGHTRED);
	arc(300,242,0,360,3);
	floodfill(300,242,border_color);
	setcolor(BLACK);
	arc(300,260 ,180,0,5);
	floodfill(300,260,border_color);
	
	setcolor(WHITE);
	line(230,335,180,285);
	line(370,335,420,285);
	
	getch();
	closegraph();
}
void christmas_tree()
{
	int gd,gm;
	int border_color = WHITE;
	gd = DETECT;
	initgraph(&gd,&gm,NULL);
	line(105,200,105,290);
	line(145,200,145,290);
	line(105,290,145,290);
	
	line(75,200,175,200);
	line(75,200,100,170);
	line(175,200,150,170);
	line(100,170,80,170);
	line(150,170,170,170);
	line(80,170,105,140);
	line(170,170,145,140);
	line(105,140,90,140);
	line(145,140,160,140);
	line(90,140,125,105);
	line(160,140,125,105);
	setfillstyle(1,6);
	floodfill(115,210,WHITE);
	setfillstyle(1,10);
	floodfill(100,150,WHITE);
	getch();
	closegraph();
}
int main()
{
	int choice;
	cout << "Enter 0 for snowman or enter 1 for christmas tree-\n";
	cin >> choice;
	if (choice == 0)
	{
		snowman();
	}
	else if (choice == 1)
	{
		christmas_tree();
	}
	return 0;
}
