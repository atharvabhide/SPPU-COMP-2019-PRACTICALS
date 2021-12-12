#include<iostream>
using namespace std;
void addition(int n1, int n2);
void multiplication(int n1, int n2);
void subtraction(int n1, int n2);
void division(int n1, int n2);

int main()
{
    int n1;
    int n2;
    cout << "Enter the first number: ";
    cin >> n1;
    cout << "Enter the second number: ";
    cin >> n2;

    addition(n1,n2);
    subtraction(n1,n2);
    multiplication(n1,n2);
    division(n1,n2);

}

void addition(int n1, int n2)
{
    int sum = n1 + n2;

    cout << "Addition of the two numbers is " << sum << endl;
}

void multiplication(int n1, int n2)
{
    int multiplication = n1 * n2;

    cout << "Multiplication of the two numbers is " << multiplication << endl;
}

void subtraction(int n1, int n2)
{
    int subtraction = n1 - n2;

    cout << "Subtraction of the two numbers is " << subtraction << endl;
}

void division(int n1, int n2)
{
    float division = (float)n1 / (float)n2;

    cout << "Division of the two numbers is " << division << endl;
}
