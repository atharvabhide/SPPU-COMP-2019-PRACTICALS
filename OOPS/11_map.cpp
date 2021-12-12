#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<string,long> m;
    cout << "Enter the number of states you want to enter-\n";
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string state;
        long population;
        cout << "Enter the state name-\n";
        cin >> state;
        cout << "Enter the population of the state-\n";
        cin >> population;
        m.insert({state,population});
    }
    cout << "Enter the state you want to search-\n";
    string key;
    cin >> key;
    auto it = m.find(key);

    if (it == m.end())
    {
        cout << "The searched state is not present in the map!\n";
    }
    else 
    {
        cout << "The population of the searched state is- " << it->second << endl;
    }
    return 0;
}
