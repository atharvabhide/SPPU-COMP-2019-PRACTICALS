#include<iostream>
#include<stdlib.h>
#include<string.h>
using namespace std;
	class stack
	{
	private :
		char c[100];
		int max,top;
	public :
		stack(int m)
		{
			if (m > 1)
				max = m;
			else
			{
				cout<<"Capacity should be a positive natural number.";
				return;
			}
			top = -1;
		}
		void push(char a)
		{
			if (top == -1)
			{
				c[0] = a;
				top = 0;
			}
			else
			{
				if(top < max-1)
				{
					top = top + 1;
					c[top] = a;
				}
				//else
				//	cout<<"Error : Capacity full!"<<endl;
			}
		}
		char pop ()
		{
			if (top == -1)
			{
				//cout<<"Error : The stack is empty.";
				char b = '#';
				return b;
			}
			else
			{
				if (top < max)
				{
					char t = c[top];
					c[top] = '\0';
					top = top - 1;
					return t;
				}
				/*if (top == 0 || top == max+1)
				{
					cout<<"Error : The stack is empty."<<endl;
				}*/
			}
		}
		char topelement ()
		{
			if (top == -1)
			{
				//cout<<"Error : The stack is empty.";
				char b = '#';
				return b;
			}
			char t = c[top];
			return t;
		}
		int isempty()
		{
			if(top == -1)
			{
				return 1;
			}
			else
				return 0;
		}
		int isfull()
		{
			if(top == max-1)
			{
				return 1;
			}
			else
				return 0;
		}
		void display()
		{
			int a = top;
			if (a == -1)
			{
				cout<<"Error : The stack is empty."<<endl;
				return;
			}
			while (a != -1)
			{
				cout<<c[a]<<"\n";
				a = a - 1;
			}
		}
	};
	class expression
	{
		char expr[50];
	public :
		expression()
		{
			expr[0] = '\0';
		}
		expression(char *s)
		{
			strcpy(expr,s);
		}
		expression(string s)
		{
			int i = s.length();
			for(int j=0; j<i; j++)
				expr[j] = s.at(j);
			expr[i] = '\0';
		}
		int FindPriority (char a)
		{
			switch(a)
			{
				case '/' :
					return 4;
				case '*' :
					return 4;
				case '+' :
					return 1;
				case '-' :
					return 1;
				case '(' :
					return -1;
				case ')' :
					return -2;
				default :
					return 0;
			}
		}
		int Verify ()
		{
			int i,count1 = 0,count2 = 0;
			for (i=0; expr[i]; i++)
			{
				if (expr[i] == '(')
					count1++;
				if (expr[i] == ')')
					count2++;
			}
			if(count1 == count2)
				return 1;
			else
				return 0;
		}
		string Infix2Postfix()
		{
			stack ob(50);
			int i,pri,k = 0;
			char postfix[50];
			for (i = 0; expr[i] != '\0'; i++)
			{
				pri = FindPriority(expr[i]);
				if (expr[i] == '(')
				{
					ob.push(expr[i]);
				}
				if (expr[i] == ')')
				{
					while(ob.isempty() != 1 && ob.topelement() != '(')
					{
							postfix[k] = ob.topelement();
							ob.pop();
							k++;
					}
					if (ob.isempty() != 1)
					{
						ob.pop();
					}
				}
				if (pri == 0)
				{
			 		postfix[k] = expr[i];
					k++;
				}
				if (pri == 1 || pri == 2 || pri == 3 || pri == 4)
				{
					if (ob.isempty() == 1)
					{
						ob.push(expr[i]);
					}
					else
					{
						while (ob.isempty() != 1 && ob.topelement() != '(' && pri <= FindPriority(ob.topelement()))
						{
							postfix[k] = ob.topelement();
							ob.pop();
							k++;
						}
						ob.push(expr[i]);
					}
				}
			}
			while (ob.isempty() != 1 )
			{
					postfix[k] = ob.topelement();
					ob.pop();
					k++;
			}
			postfix[k] = '\0';
			return postfix;
		}
		float evaluation (string p)
		{
			int n;
			cout<<"Enter the number of variables in the expression : ";
			cin>>n;
			cout<<"Enter the value of variables in the format : variable value (Eg. a 5 b 4 c 3)"<<endl;
			char variable[10];
			int i,j,k,pri;
			float value [10];
			for (i = 0; i < n; i++)
			{
				cin>>variable[i]>>value[i];
			}
			expression post(p);
			stack obj(50);
			int pos1,pos2;
			float num1,num2;
			float res;
			char r = 'q';
			for (i = 0; post.expr[i] ; i++)
			{
				pri = FindPriority(post.expr[i]);
				cout<<post.expr[i]<<"\t"<<pri<<endl;
				if (pri == 0)
				{
			 		obj.push(post.expr[i]);
					cout<<"push operand "<<post.expr[i]<<endl;
				}
				else// (pri == 1 || pri == 2 || pri == 3 || pri == 4)
				{
					char x = obj.pop();
					char y = obj.pop();
					cout<<"popped 2 operands "<<x<<"\t"<<y<<endl;
					for(j = 0; variable[j]; j++)
					{
						if (variable[j] == x)
						{
							pos1 = j;
							break;
						}
					}
					for(k = 0; variable[k]; k++)
					{
						if (variable[k] == y)
						{
							pos2 = k;
							break;
						}
					}
					num1 = value[pos1];
					num2 = value[pos2];
					switch(post.expr[i])
					{
						case '/' :
							res = num2/num1;
							cout<<"result "<<res<<endl;
							break;
						case '*' :
							res = num2*num1;cout<<"result "<<res<<endl;
							break;
						case '+' :
							res = num2+num1;cout<<"result "<<res<<endl;
							break;
						case '-' :
							res = num2-num1;cout<<"result "<<res<<endl;
							break;
					}
					//cout<<n;
					int a = int(r);
					a++;
					r = char(a);
					variable[n] = r;
					value[n] = res;

					//if(obj.isempty() == 1)
						obj.push(variable[n]);
						cout<<"push "<<variable[n]<<endl;
					n++;
					//int(r) = r + 1;
				}
			cout<<"display"<<endl;
			obj.display();
			cout<<endl<<endl;
			}

			for(j = 0; variable[j]; j++)
			{
				//cout<<"variable"<<variable[j]<<endl;
				if (variable[j] == obj.topelement())
				{
					pos1 = j;
					break;
				}
			}
			return value[pos1];
		}




	};
	int main ()
	{
		int choice;
		char e[50];
		do{
		cout<<"Enter the expression : ";
		cin>>e;
		expression obj(e);
		int t = obj.Verify();
		if (t == 0)
		{
			cout<<"Error : Unbalanced parenthesis in the expression."<<endl;
			return 0;
		}
		string p = obj.Infix2Postfix();
		cout<<"The infix notation is : "<<e<<endl;
		cout<<"The postfix notation is : "<<p<<endl;
		float result = obj.evaluation(p);
		cout<<"The result is : "<<result<<endl<<endl;
		cout<<"Press 1 to continue \t Press 0 to exit \t";
		cin>>choice;
		}while(choice == 1);
		return 0;
	}
