#include<bits/stdc++.h>
using namespace std;

struct Student
{
    int roll_number;
    string name;
    string division;
    string address;
};

void add_students()
{
    Student s;
    cout << "Enter the roll number of the student-\n";
    cin >> s.roll_number;
    cout << "Enter the name of the student-\n";
    cin >> s.name;
    cout << "Enter the division of the student-\n";
    cin >> s.division;
    cout << "Enter the address of the student-\n";
    cin >> s.address;

    if (1 <= s.roll_number and s.roll_number <= 10)
    {
        ofstream write;
        write.open("1to10.txt", ios::app);

        write << "\n" << s.roll_number;
        write << "\n" << s.name;
        write << "\n" << s.division;
        write << "\n" << s.address;

        write.close();
    }
    if (11 <= s.roll_number and s.roll_number <= 20)
    {
        ofstream write;
        write.open("11to20.txt", ios::app);

        write << "\n" << s.roll_number;
        write << "\n" << s.name;
        write << "\n" << s.division;
        write << "\n" << s.address;

        write.close();
    }
    if (21 <= s.roll_number and s.roll_number <= 30)
    {
        ofstream write;
        write.open("21to30.txt", ios::app);

        write << "\n" << s.roll_number;
        write << "\n" << s.name;
        write << "\n" << s.division;
        write << "\n" << s.address;

        write.close();
    }
    if (31 <= s.roll_number and s.roll_number <= 40)
    {
        ofstream write;
        write.open("31to40.txt", ios::app);

        write << "\n" << s.roll_number;
        write << "\n" << s.name;
        write << "\n" << s.division;
        write << "\n" << s.address;

        write.close();
    }
    if (41 <= s.roll_number and s.roll_number <= 50)
    {
        ofstream write;
        write.open("41to50.txt", ios::app);

        write << "\n" << s.roll_number;
        write << "\n" << s.name;
        write << "\n" << s.division;
        write << "\n" << s.address;

        write.close();
    }
}

void print(Student s)
{
    cout << "Roll number: " << s.roll_number << endl;
    cout << "Name: " << s.name << endl;
    cout << "Division: " << s.division << endl;
    cout << "Address: " << s.address << endl;
}

void display_students()
{
    Student s1;
    ifstream read;
    read.open("1to10.txt");
    while (!read.eof())
    {
        read >> s1.roll_number;
        read >> s1.name;
        read >> s1.division;
        read >> s1.address;

        print(s1);
    }
    read.close();

    cout << endl;

    Student s2;
    read.open("11to20.txt");
    while (!read.eof())
    {
        read >> s2.roll_number;
        read >> s2.name;
        read >> s2.division;
        read >> s2.address;

        print(s2);
    }
    read.close();

    cout << endl;

    Student s3;
    read.open("21to30.txt");
    while (!read.eof())
    {
        read >> s3.roll_number;
        read >> s3.name;
        read >> s3.division;
        read >> s3.address;

        print(s3);
    }
    read.close();

    cout << endl;

    Student s4;
    read.open("31to40.txt");
    while (!read.eof())
    {
        read >> s4.roll_number;
        read >> s4.name;
        read >> s4.division;
        read >> s4.address;

        print(s4);
    }
    read.close();

    cout << endl;

    Student s5;
    read.open("41to50.txt");
    while (!read.eof())
    {
        read >> s5.roll_number;
        read >> s5.name;
        read >> s5.division;
        read >> s5.address;

        print(s5);
    }
    read.close();

    cout << endl;
}

int search_students(int roll_number)
{
    if (1 <= roll_number and roll_number <= 10)
    {
        Student s;
        ifstream read;
        read.open("1to10.txt");
        while (!read.eof())
        {
            read >> s.roll_number;
            read >> s.name;
            read >> s.division;
            read >> s.address;
            if (s.roll_number == roll_number)
            {
                cout << "Student's record found!" << endl;
                return roll_number;
            }
        }

        read.close();
    }
    if (11 <= roll_number and roll_number <= 20)
    {
        Student s;
        ifstream read;
        read.open("11to20.txt");
        while (!read.eof())
        {
            read >> s.roll_number;
            read >> s.name;
            read >> s.division;
            read >> s.address;
            if (s.roll_number == roll_number)
            {
                cout << "Student's record found!" << endl;
                return roll_number;
            }
        }

        read.close();
    }
    if (21 <= roll_number and roll_number <= 30)
    {
        Student s;
        ifstream read;
        read.open("21to30.txt");
        while (!read.eof())
        {
            read >> s.roll_number;
            read >> s.name;
            read >> s.division;
            read >> s.address;
            if (s.roll_number == roll_number)
            {
                cout << "Student's record found!" << endl;
                return roll_number;
            }
        }

        read.close();
    }
    if (31 <= roll_number and roll_number <= 40)
    {
        Student s;
        ifstream read;
        read.open("31to40.txt");
        while (!read.eof())
        {
            read >> s.roll_number;
            read >> s.name;
            read >> s.division;
            read >> s.address;
            if (s.roll_number == roll_number)
            {
                cout << "Student's record found!" << endl;
                return roll_number;
            }
        }

        read.close();
    }
    if (41 <= roll_number and roll_number <= 50)
    {
        Student s;
        ifstream read;
        read.open("41to50.txt");
        while (!read.eof())
        {
            read >> s.roll_number;
            read >> s.name;
            read >> s.division;
            read >> s.address;
            if (s.roll_number == roll_number)
            {
                cout << "Student's record found!" << endl;
                return roll_number;
            }
        }

        read.close();
    }

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
    
    if (1 <= roll_number and roll_number <= 10)
    {
        Student s;
        ifstream read;
        ofstream write;
        read.open("1to10.txt");
        write.open("temp.txt");
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
        read.close();
        write.close();
        remove("1to10.txt");
        rename("temp.txt", "1to10.txt");
    }
    if (11 <= roll_number and roll_number <= 20)
    {
        Student s;
        ifstream read;
        ofstream write;
        read.open("11to20.txt");
        write.open("temp.txt");
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
        read.close();
        write.close();
        remove("11to20.txt");
        rename("temp.txt", "11to20.txt");
    }
    if (21 <= roll_number and roll_number <= 30)
    {
        Student s;
        ifstream read;
        ofstream write;
        read.open("21to30.txt");
        write.open("temp.txt");
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
        read.close();
        write.close();
        remove("21to30.txt");
        rename("temp.txt", "21to30.txt");
    }
    if (31 <= roll_number and roll_number <= 40)
    {
        Student s;
        ifstream read;
        ofstream write;
        read.open("31to40.txt");
        write.open("temp.txt");
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
        read.close();
        write.close();
        remove("31to40.txt");
        rename("temp.txt", "31to40.txt");
    }
    if (41 <= roll_number and roll_number <= 50)
    {
        Student s;
        ifstream read;
        ofstream write;
        read.open("1to10.txt");
        write.open("temp.txt");
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
        read.close();
        write.close();
        remove("41to50.txt");
        rename("temp.txt", "41to50.txt");
    }
}

int main()
{
    add_students();
    add_students();
    add_students();
    add_students();
    add_students();
    add_students();

    display_students();

    int found = search_students(34);
    if (found == -1) 
    {
        cout << "Record not found!" << endl;
        cout << endl;
    }

    delete_students(7);
    display_students();
    return 0;
}
