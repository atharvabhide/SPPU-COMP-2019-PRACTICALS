#include<iostream>
#include<graphics.h>
#include<math.h>
using namespace std;
class scan
{
	int n,i,k;
	int x[10],y[10],xint[10];
	float dx,dy,slope[30];
	public:
	void slope1();
	void drawpoly();
};
void scan::drawpoly()
{
	cout<<"\nEnter number of edges- ";
	cin>>n;
	cout<<"\nEnter co-ordinates of "<<n<<"points- ";
	for(i=0;i<n;i++)
	{
		cout<<"\nPoint "<<i+1<<"- ";
		cin>>x[i];
		cin>>y[i];
	}
	x[n]=x[0];
	y[n]=y[0];
}
void scan::slope1()
{
	for(i=0;i<n;i++)
	line(x[i],y[i],x[i+1],y[i+1]);
	int temp;
	for(i=0;i<n;i++)
	{
		dy=y[i+1]-y[i];
		dx=x[i+1]-x[i];
		if(dy==0)
		slope[i]=1;
		else if(dx==0)
		slope[i]=0;
		else
		slope[i]=dx/dy;
	}
	for(int c=0;c<480;c++ )
	{
		k=0;
		for(i=0;i<n;i++)
		{
			if((y[i]<=c && y[i+1]>c) || (y[i]>c && y[i+1]<=c))
			{
				xint[k]=x[i]+slope[i]*(c-y[i]);
				k++;
			}
		}
		for(int j=0;j<k-1;j++)
		{
			for(i=0;i<k-1;i++)
			{
				if(xint[i]>xint[i+1])
				{
					temp=xint[i];
					xint[i]=xint[i+1];
					xint[i+1]=temp;
				}
			}
		}
		for(i=0;i<k;i=i+2)
		{
			setcolor(9);
			line(xint[i],c,xint[i+1],c);
			delay(100);
		}
	}
}
int main()
{
	int gd=DETECT,gm;
	
	scan s;
	s.drawpoly();
	initgraph(&gd,&gm,NULL);
	s.slope1();
	getch();
	closegraph();
	return 0;
}
