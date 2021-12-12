#include <bits/stdc++.h>
using namespace std;
class Person
{
public:
    string name;
    int birth_date;
    long phone_number;
    void get()
    {
        cout << "Enter the name of the person-\n";
        cin >> name;
        cout << "Enter birth date of the person-\n";
        cin >> birth_date;
        cout << "Enter phone number of the person-\n";
        cin >> phone_number;
    }
    void display()
    {
        cout << endl;
        cout << "The name of the person is- " << name << endl;
        cout << "The birth date of the person is- " << birth_date << endl;
        cout << "The phone number of the person is- " << phone_number << endl;
        cout << endl;
    }
};
bool cmp(Person &p1, Person &p2)
{
    return p1.name < p2.name;
}
int main()
{
    int n;
    cout << "ENTER THE NUMBER OF PERSONS HERE-\n";
    cin >> n;
    vector<Person> v(n);
    vector<string> names(n);
    char choice1;
    cout << "Do you want to start/continue? Press Y or else press N to terminate!\n";
    cin >> choice1;
    while (choice1 == 'y' or choice1 == 'Y')
    {
        int operation;
        cout << endl;
        cout << "Enter 1 for inserting the records" << endl;
        cout << "Enter 2 for displaying the person's record" << endl;
        cout << "Enter 3 for sorting the record" << endl;
        cout << "Enter 4 for searching a person's record" << endl;
        cout << "Enter 5 for terminating the program" << endl;
        cin >> operation;
        if (operation == 5)
        {
            break;
        }
        switch (operation)
        {
        case 1:
            for (int i = 0; i < n; i++)
            {
                v[i].get();
            }
            break;
        case 2:
            for (int i = 0; i < n; i++)
            {
                v[i].display();
            }
            break;
        case 3:
            sort(v.begin(), v.end(), cmp);
            break;
        case 4:
            for (int i = 0; i < n; i++)
            {
                names.push_back(v[i].name);
            }
            string key;
            cout << "Enter the name to be searched in the record-\n";
            cin >> key;
            if (binary_search(names.begin(), names.end(), key))
            {
                cout << "THE PERSON'S DATA IS PRESENT IN THE RECORD\n";
            }
            else
            {
                cout << "THE PERSON'S DATA IS NOT PRESENT IN THE RECORD\n";
            }
            break;
        }
    }
    cout << "The program has been terminated!";
    return 0;
}
