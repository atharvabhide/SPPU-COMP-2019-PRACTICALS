#include<bits/stdc++.h>
using namespace std;

int main()
{

    int n;
    cout << "Enter the number of pages here-\n";
    cin >> n;

    int pages[n];
    cout << "Enter the page numbers here-\n";
    for (int i = 0; i < n; i++)
    {
        cin >> pages[i];
    }

    int capacity;
    cout << "Enter the capacity of the memory-\n";
    cin >> capacity;

    queue<int> q;
    unordered_set<int> memory;

    int pf = 0;
    int ph = 0;

    for (int i = 0; i < n; i++)
    {
        // check if memory holds fewer pages than capacity
        if (memory.size() < capacity)
        {
            // push page in the memory if it is not in the memory
            if (memory.find(pages[i]) == memory.end())
            {
                memory.insert(pages[i]);
                pf++;
                q.push(pages[i]);
            } 
            else
            {
                ph++;
            }
        }
        // here, size of memory is full
        else
        {   
            // check if page is in memory
            if (memory.find(pages[i]) == memory.end())
            {
                int val = q.front();
                q.pop();
                memory.erase(val);
                memory.insert(pages[i]);
                q.push(pages[i]);
                pf++;
            }
            else
            {
                ph++;
            }
        }
    }

    cout << "Hit ratio is-" << endl;
    cout << float(ph)/float(n) << endl;

    cout << "Fault ratio is-" << endl;
    cout << float(pf)/float(n) << endl; 
    return 0;
}
