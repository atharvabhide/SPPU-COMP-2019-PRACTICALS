#include<bits/stdc++.h>
#include "page_replacement_utils.h"
using namespace std;

int main()
{
    auto [pages, capacity] = readPages();
    int n = pages.size();
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
            if ((int)memory.size() < capacity)
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

    printPageStats(ph, pf, n);

    return 0;
}
