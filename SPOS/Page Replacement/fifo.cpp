#include<bits/stdc++.h>
#include "page_replacement_utils.h"
using namespace std;

int main()
{
    auto [pages, capacity] = readPages();
    int n = pages.size();

    queue<int> q;
    unordered_set<int> memory;

    int pf = 0;
    int ph = 0;

    for (int i = 0; i < n; i++)
    {
        // check if memory holds fewer pages than capacity
        if ((int)memory.size() < capacity)
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

    printPageStats(ph, pf, n);
    return 0;
}
