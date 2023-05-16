#include<graphics.h>
#include<math.h>

using namespace std;

class circle1
{
	public:
		float x,y;
		int r,d;
		float x1,y1,x2,y2,dx,dy,length,i;
		void draw_bressenham(int i);
		void dda(int x1,int y1,int x2, int y2);
				
};
void circle1::draw_bressenham(int i)
{
	r=i;
	x=0;
	y=r;
	d=3-(2*r);
	
	while(x<y)
	{
		
		putpixel(200+x,200+y,WHITE);
		putpixel(200+y,200+x,WHITE);
		putpixel(200+y,200-x,WHITE);
		putpixel(200+x,200-y,WHITE);
		putpixel(200-x,200+y,WHITE);
		putpixel(200-y,200+x,WHITE);
		putpixel(200-y,200-x,WHITE);
		putpixel(200-x,200-y,WHITE);
		if(d<0)
		{
			d=d+(4*x+6);	
		}
		else
		{
			d=d+(4*(x-y))+10;
			y=y-1;
		}
		x=x+1;
	}

	
}
void circle1::dda(int x1,int y1,int x2,int y2)
{
	if (abs(x2-x1)>abs(y2-y1))
	{
		length=abs(x2-x1);
	}
	else{length=abs(y2-y1);}
	dx=(x2-x1)/length;
	dy=(y2-y1)/length;
	x=x1+0.5;
	y=y1+0.5;
	i=0;
	while(i<length)
	{
		putpixel(x,y,WHITE);
		x=x+dx;
		y=y+dy;
		i++;
	}
}
int main()
{
	circle1 obj[5];
	int gm,gd,i;
	gd=DETECT;
	i=100;
	initgraph(&gd,&gm,NULL);
	obj[0].draw_bressenham(i);
	i=i/2;
	obj[1].draw_bressenham(i);
	obj[2].dda(115,250,200,100);
	obj[2].dda(115,250,288,250);
	obj[2].dda(288,250,200,100);
	getch();
	closegraph();
	return 0;
}

