#include <iostream>
using namespace std;

class Student
{
    int roll_number;
    char name[10];
    int marks;
public:
    void get_data();
    void display_data();
};

void Student::get_data()
{
    cout << "Enter the roll number-" << endl;
    cin >> roll_number;
    cout << "Enter the name-" << endl;
    cin >> name;
    cout << "Enter the marks-" << endl;
    cin >> marks;
}

void Student::display_data()
{
    cout << "Roll number of the student is- " << roll_number << endl;
    cout << "Name of the student is- " << name << endl;
    cout << "Marks of the student are- " << marks << endl;
}

int main()
{
    Student s1;
    s1.get_data();
    s1.display_data();
    return 0;
}
