#ifndef PAGE_REPLACEMENT_UTILS_H
#define PAGE_REPLACEMENT_UTILS_H

#include <iostream>
#include <vector>

using namespace std;

/**
 * Read page reference string from stdin.
 * Returns: pair of (pages vector, capacity).
 */
inline pair<vector<int>, int> readPages()
{
    int n;
    cout << "Enter the number of pages here-\n";
    cin >> n;

    vector<int> pages(n);
    cout << "Enter the page numbers here-\n";
    for (int i = 0; i < n; i++)
    {
        cin >> pages[i];
    }

    int capacity;
    cout << "Enter the capacity of the memory-\n";
    cin >> capacity;

    return {pages, capacity};
}

/**
 * Print page-hit and page-fault statistics.
 */
inline void printPageStats(int ph, int pf, int total)
{
    cout << "Number of page hits: " << ph << endl;
    cout << "Number of page faults: " << pf << endl;
    cout << "Hit ratio: " << float(ph) / float(total) << endl;
    cout << "Fault ratio: " << float(pf) / float(total) << endl;
}

#endif // PAGE_REPLACEMENT_UTILS_H
