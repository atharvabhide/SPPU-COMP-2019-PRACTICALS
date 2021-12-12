#include<bits/stdc++.h>
using namespace std;
class publication
{
protected:
    string title;
    float price;
public:
    publication(string title = "", float price = 0.0f)
    {
        this->title = title;
        this->price = price;
    }
};

class book:public publication
{
private:
    int page_count;
public:
    book(string title,float price,int page_count) : publication(title,price)
    {
        this->page_count = page_count;
    }
    void display()
    {
        cout << "Title of the book is- " << title << endl;
        cout << "Price of the book is- " << price << endl;
        cout << "The page count is- " << page_count << endl;
    }
};

class tape:public publication
{
private:
    float playing_time;
public:
    tape(string title,float price,float playing_time) : publication(title,price)
    {
        this->playing_time = playing_time;
    }
    void display()
    {
        cout << "Title of the tape is- " << title << endl;
        cout << "Price of the tape is- " << price << endl;
        cout << "The playing time is- " << playing_time << endl;
    }
};

int main()
{
    string title;
    float price;
    int page_count;
    float playing_time;
    char option;
    char choice;
    do 
    {
        cout << "Do you want to start/continue?-(press Y/N) " << endl;
        cin >> option;
        if (option=='n' or option=='N')
        {
            break;
        }
        cout << "Welcome to generic publication company!\nEnter B for book\nEnter T for tape\n";
        cin >> choice;
        switch (choice)
        {
        case 'B':
        {
            cout << "Enter title of the book- " << endl;
            cin >> title;
            cout << "Enter the price of the book- " << endl;
            cin >> price;
            cout << "Enter the number of pages in the book- " << endl;
            cin >> page_count;
            book b1(title,price,page_count);
            b1.display();
            break;
        }
        case 'T':
        {
            cout << "Enter title of the tape- " << endl;
            cin >> title;
            cout << "Enter the price of the tape- " << endl;
            cin >> price;
            cout << "Enter the playing time of the tape- " << endl;
            cin >> playing_time;
            tape t1(title,price,playing_time);
            t1.display();
            break;
        }
        default:
            cout << "Enter a valid choice!" << endl;
            break;
        }
    }while(option == 'Y' or option == 'y');
    
    return 0;
}
