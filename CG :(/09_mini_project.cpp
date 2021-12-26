#include<conio.h>
#include<graphics.h>
#include<dos.h>
int main()
{
int gd=DETECT,gm,i=0;
initgraph(&gd,&gm,NULL);
for(i;i<600;i++)
{
line(80+i,300-i,250+i,300-i);
line(150+i,340-i,200+i,340-i);
line(150+i,340-i,100+i,400-i);
line(200+i,340-i,100+i,400-i);
line(80+i,380-i,115+i,380-i);
line(132+i,380-i,250+i,380-i);
ellipse(250+i,340-i,270,90,80,40);
line(100+i,270-i,150+i,300-i);
line(100+i,270-i,200+i,300-i);
line(80+i,300-i,65+i,260-i);
arc(80+i,340-i,180,270,40);

line(40+i,340-i,40+i,260-i);
line(40+i,260-i,65+i,260-i);
ellipse(250+i,338-i,10,81,70,30);
line(261+i,333-i,320+i,333-i);
line(261+i,333-i,261+i,310-i);
rectangle(100+i,310-i,120+i,330-i);
rectangle(130+i,310-i,150+i,330-i);
rectangle(160+i,310-i,180+i,330-i);
rectangle(190+i,310-i,210+i,330-i);
rectangle(220+i,310-i,240+i,330-i);
//
line(0,459,679,459);

rectangle(510-i,459,550-i,430) ;
rectangle(550-i,459,610-i,430);
line(530-i,410,550-i,430);
line(530-i,410,510-i,430);
line(590-i,410,610-i,430);
line(590-i,410,530-i,410);

rectangle(430-i,430,490-i,459);
rectangle(390-i,430,430-i,459);
line(410-i,410,430-i,430);
line(410-i,410,390-i,430);
line(410-i,410,470-i,410);
line(470-i,410,490-i,430);

delay(10);
cleardevice();
}
getch();
}
