#include<bits/stdc++.h>
using namespace std;
class User
{
public:
    int age;
    int income;
    string city;
    bool vehicle;
    User()
    {
        age = 0;
        income = 0;
        city = "";
        vehicle = 0;
    }
    void get()
    {
        cout << "Enter the age of the user-\n";
        cin >> age;

        cout << "Enter the income of the user-\n";
        cin >> income;
        
        cout << "Enter the user's city-\n";
        cin >> city;

        cout << "Enter 0 if the user does not have a vehicle else enter 1-\n";
        cin >> vehicle;
    }
};
class MyException1 : public exception, public User
{
public:
    const char* what() const throw()
    {
        return "User's age is not between 18 and 55!\n";
    }
};
class MyException2 : public exception, public User
{
public:
    const char* what() const throw()
    {
        return "User's income is not between 50000 and 100000!\n";
    }
};
class MyException3 : public exception, public User 
{
public:
    const char* what() const throw()
    {
        return "User does not stay in Pune or Mumbai or Bangalore or Chennai!\n";
    }
};
class MyException4: public exception, public User
{
public:
    const char* what() const throw()
    {
        return "User does not have a 4 wheeler!\n";
    }
};
int main()
{
    User u;
    u.get();
    try 
    {
        if (u.age < 18 or u.age > 55)
        {
            throw MyException1();
        }        
        else if (u.income < 50000 or u.income > 100000)
        {
            throw MyException2();
        }
        else if ((u.city != "Pune") and (u.city != "Mumbai") and (u.city != "Bangalore") and (u.city != "Chennai"))
        {
            throw MyException3();
        }
        else if (u.vehicle == 0)
        {
            throw MyException4();
        }
    }
    catch (MyException1 &e1)
    {
        cout << e1.what();
    }
    catch (MyException2 &e2)
    {
        cout << e2.what();
    }
    catch (MyException3 &e3)
    {
        cout << e3.what();
    }
    catch (MyException4 &e4)
    {
        cout << e4.what();
    }
    catch (exception &e)
    {
        cout << "Some other unknown exception has occured\n";
    }
    return 0;
}
