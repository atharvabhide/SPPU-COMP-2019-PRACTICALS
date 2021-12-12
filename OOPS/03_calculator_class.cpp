#include <bits/stdc++.h>
using namespace std;
class Calculator
{
private:
    int no1;
    int no2;
    char operation;
public:
    Calculator(int no1, int no2, char operation)
    {
        this->no1 = no1;
        this->no2 = no2;
        this->operation = operation;
    }
    void addition()
    {
        int addition = no1 + no2;
        cout << "Addition is " << addition << endl;
    }
    void subtraction()
    {
        int subtraction = no1 - no2;
        cout << "Subtraction is " << subtraction << endl;
    }
    void multiplication()
    {
        int multiplication = no1 * no2;
        cout << "Multiplication is " << multiplication << endl;
    }
    void division()
    {
        int division = no1 / no2;
        cout << "Division is " << division << endl;
    }
};
int main() 
{
    int t;
    cout << "Enter the number of test cases-\n";
    cin >> t;
    while (t--)
    {
        int no1,no2;
        char operation;
        cout << "Enter the two numbers here-\n";
        cin >> no1 >> no2;
        cout << "Enter the operator here-\nAddition = +\nSubtraction = -\nMultiplication = *\nDivision = /\n";
        cin >> operation;
        Calculator calci(no1, no2, operation);
        switch(operation)
        {
            case '+':
                calci.addition();
                break;
            case '-':
                calci.subtraction();
                break;
            case '*':
                calci.multiplication();
                break;
            case '/':
                calci.division();
                break;
            default:
                cout << "Please enter a valid operator!" << endl;
        }
    }
	return 0;
}
