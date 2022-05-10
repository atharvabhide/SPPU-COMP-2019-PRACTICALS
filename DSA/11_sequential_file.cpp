#include<bits/stdc++.h>
#include<fstream>
using namespace std;

struct Student
{
    int roll_number;
    string name;
    char division;
    string address;
};

void add_students()
{
    Student s;
    cout << "Enter the roll number of the student to be added-\n";
    cin >> s.roll_number;
    cout << "Enter the name of the student to be added-\n";
    cin >> s.name;
    cout << "Enter the division of the student to be added-\n";
    cin >> s.division;
    cout << "Enter the address of the student to be added-\n";
    cin >> s.address;

    ofstream write;
    write.open("students.txt", ios::app);

    write << "\n" << s.roll_number;
    write << "\n" << s.name;
    write << "\n" << s.division;
    write << "\n" << s.address;

    write.close();
}

void display(Student s)
{
    cout << "Roll Number- " << s.roll_number << endl;
    cout << "Name- " << s.name << endl;
    cout << "Division- " << s.division << endl;
    cout << "Address- " << s.address << endl;
    cout << endl;
}

void read_students()
{
    Student s;
    ifstream read;
    read.open("students.txt");

    while (!read.eof())
    {
        read >> s.roll_number;
        read >> s.name;
        read >> s.division;
        read >> s.address;

        display(s);
    }

    read.close();
}

int search_students(int roll_number)
{
    Student s;

    ifstream read;
    read.open("students.txt");

    while (!read.eof())
    {
        read >> s.roll_number;
        read >> s.name;
        read >> s.division;
        read >> s.address;

        if (s.roll_number == roll_number)
        {
            cout << "Student's record found!" << endl;
            return s.roll_number;
        }
    }

    read.close();
    cout << "Student's record not found!" << endl;
    return -1;
}

void delete_students(int roll_number)
{
    roll_number = search_students(roll_number);

    if (roll_number == -1)
    {
        cout << "Student record to be deleted is not present in the file!" << endl;
        return;
    }
    else
    {
        Student s;

        ofstream write;
        write.open("temp.txt", ios::app);

        ifstream read;
        read.open("students.txt");

        while (!read.eof())
        {
            read >> s.roll_number;
            read >> s.name;
            read >> s.division;
            read >> s.address;

            if (s.roll_number != roll_number)
            {
                write << "\n" << s.roll_number;
                write << "\n" << s.name;
                write << "\n" << s.division;
                write << "\n" << s.address;
            }
        }

        write.close();
        read.close();

        remove("students.txt");
        rename("temp.txt", "students.txt");
        
        cout << "Student record to be deleted is deleted successfully!" << endl;
    }
}

int main()
{
    int choice;
    do 
    {
        cout << "-----STUDENT RECORDS-----" << endl;
        cout << "Enter 1 for adding a record" << endl;
        cout << "Enter 2 for displaying the records" << endl;
        cout << "Enter 3 for searching a record" << endl;
        cout << "Enter 4 for deleting a record" << endl;
        cout << "Enter 0 to exit" << endl;
        cin >> choice;

        switch (choice)
        {
        case 1:
            add_students();
            break;
        case 2:
            read_students();
            break;
        case 3:
            int roll_number;
            cout << "Enter roll number of the student to be searched-\n";
            cin >> roll_number;
            search_students(roll_number);
            break;
        case 4:
            cout << "Enter roll number of the student to be deleted-\n";
            cin >> roll_number;
            delete_students(roll_number);
            break;
        case 0:
            break;
        }
    } while (choice != 0);
}
