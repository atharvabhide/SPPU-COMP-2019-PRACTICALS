#include<bits/stdc++.h>
using namespace std;

int main()
{

    int n;
    cout << "Enter the number of pages here-\n";
    cin >> n;

    vector<int> pages;
    cout << "Enter the page numbers here-\n";
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        pages.push_back(x);
    }

    int capacity;
    cout << "Enter the capacity here-\n";
    cin >> capacity;
    vector<int> memory;

    int ph = 0;
    int pf = 0;

    for (int i = 0; i < n; i++)
    {
        if (find(memory.begin(), memory.end(), pages[i]) != memory.end())
        {   
            memory.erase(find(memory.begin(), memory.end(), pages[i]));
            memory.push_back(pages[i]);
            ph++;
        }
        else 
        {
            pf++; 
            if (memory.size() < capacity)
            {
                memory.push_back(pages[i]);
            }
            else
            {
                memory.erase(memory.begin());
                memory.push_back(pages[i]);
            }
        }
    }

    cout << "Number of page hits are- " << ph << endl;
    cout << "Number of page faults are- " << pf << endl;

    return 0;
}
