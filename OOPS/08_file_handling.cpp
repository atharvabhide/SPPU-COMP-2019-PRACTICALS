# include<iostream>
# include<fstream>
# include<cstring>
using namespace std;

int main()
{
	fstream fobj;
	fobj.open("File3.txt", ios::out);
	char arr[100];
	cout<<"Enter your data:- \n";
	cin.getline(arr,100);
	int length=strlen(arr);
	fobj.write(arr,length);
	fobj.close();
	char line[100];
	fobj.open("File3.txt", ios::in);
    cout << "Entered data is-\n";
	while(fobj)
	{
		fobj.getline(line, length+1);
		cout<<line;
	}
	fobj.close();
	return 0;
}
