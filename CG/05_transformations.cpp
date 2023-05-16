#include<iostream>
#include<graphics.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>
#include<dos.h>

using namespace std;

float imat[3][3]={{1,0,0},{0,1,0},{0,0,1}};

class Matrix
{
	float sx,sy,tx,ty,ang;
public:
	float a[3][3];

	Matrix()
	{

	}
	void setS(float x, float y)
	{
		sx = x;
		sy = y;
		imat[0][0] = sx;
		imat[1][1] = sy;
	}
	void setT(float x, float y)
	{
		tx = x;
		ty = y;
		imat[2][0] = tx;
		imat[2][1] = ty;
		imat[0][0] = 1;
		imat[1][1] = 1;
	}
	void setA(float a)
	{
		ang = a;
		imat[0][0] = cos((3.142/180)*ang);
		imat[0][1] = sin((3.142/180)*ang);
		imat[1][0] = -sin((3.142/180)*ang);
		imat[1][1] = cos((3.142/180)*ang);
		imat[2][0] = 0;
		imat[2][1] = 0;
	}

	// scaling 
	Matrix operator*(Matrix &m) {
		Matrix c;
		int i=0,j=0,k=0;

		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				c.a[i][j] = 0;

		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				for(k=0;k<3;k++)
					c.a[i][j] += a[i][k]*imat[k][j];
		return c;
	}
	// translation
	Matrix operator+(Matrix &m)
	{
		Matrix c;
		int i=0,j=0,k=0;

		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				c.a[i][j] = 0;

		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				for(k=0;k<3;k++)
					c.a[i][j] += a[i][k]*imat[k][j];
		return c;
	}
	// rotation
	Matrix operator/(Matrix &m)
	{
		Matrix c;
		int i=0,j=0,k=0;

		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				c.a[i][j] = 0;

		for(i=0;i<3;i++)
			for(j=0;j<3;j++)
				for(k=0;k<3;k++)
					c.a[i][j] += a[i][k]*imat[k][j];
		return c;
	}

};


int main()
{

	system("cls");
	cout << "HELLO"<<endl;
	float sx,sy,tx,ty,angle;
	int choice;
	char ans;
	int xmid = 320,ymid=240;
	int gd = DETECT,gm;
	initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
	setcolor(WHITE);
	line(320,0,320,480);
	setcolor(WHITE);
	line(0,240,640,240);
	Matrix d,w;
	setcolor(WHITE);
	line(50+xmid, ymid-40, 70+xmid,ymid-90);
	setcolor(WHITE);
	line(90+xmid, ymid-40, 50+xmid,ymid-40);
	setcolor(WHITE);
	line(xmid+70,ymid-90, xmid+90, ymid-40);

	d.a[0][0] = 50;
	d.a[0][1] = 40;
	d.a[0][2] = 1;
	d.a[1][0] = 70;
	d.a[1][1] = 90;
	d.a[1][2] = 1;
	d.a[2][0] = 90;
	d.a[2][1] = 40;
	d.a[2][2] = 1;

	do
	{
		cout <<"\n1.Scaling\n2.Translation\n3.Rotation\n4.End\nEnter your choice: "<<endl;
		cin >> choice;
		switch (choice) {
			case 1:
				cout <<"Enter Scaling Factors:"<<endl;
				cout <<"Sx = ";
				cin >> sx;
				cout <<"Sy = ";
				cin >> sy;
				d.setS(sx,sy);
				w = d*d;
				setcolor(YELLOW);
				line(xmid+w.a[0][0],ymid-w.a[0][1],xmid+w.a[1][0],ymid-w.a[1][1]);
				line(xmid+w.a[1][0],ymid-w.a[1][1],xmid+w.a[2][0],ymid-w.a[2][1]);
				line(xmid+w.a[2][0],ymid-w.a[2][1],xmid+w.a[0][0],ymid-w.a[0][1]);
				break;
			case 2:
				cout <<"Enter Translation factors :"<<endl;
				cout <<"Tx = ";
				cin >> tx;
				cout <<"Ty = ";
				cin >> ty;
				d.setT(tx,ty);
				w = d+d;
				setcolor(GREEN);
				line(xmid+w.a[0][0],ymid-w.a[0][1],xmid+w.a[1][0],ymid-w.a[1][1]);
				line(xmid+w.a[1][0],ymid-w.a[1][1],xmid+w.a[2][0],ymid-w.a[2][1]);
				line(xmid+w.a[2][0],ymid-w.a[2][1],xmid+w.a[0][0],ymid-w.a[0][1]);
				break;
			case 3:
				cout <<"Enter Rotation Angle(-/+) = ";
				cin >>angle;
				d.setA(angle);
				w = d/d;
				setcolor(RED);
				line(xmid+w.a[0][0],ymid-w.a[0][1],xmid+w.a[1][0],ymid-w.a[1][1]);
				line(xmid+w.a[1][0],ymid-w.a[1][1],xmid+w.a[2][0],ymid-w.a[2][1]);
				line(xmid+w.a[2][0],ymid-w.a[2][1],xmid+w.a[0][0],ymid-w.a[0][1]);
				break;
		}
	}while(choice!=4);

	delay(1000);
	closegraph();
	getch();
	return 0;
}
