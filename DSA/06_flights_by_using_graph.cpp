#include<bits/stdc++.h>
using namespace std;
#define MAX 100

struct Graph
{
    int data[MAX][MAX];
    int vertices;

    map<pair<string,string>, int> hash;

    void read()
    {
        for (int i = 0; i < MAX; i++)
        {
            for (int j = 0; j < MAX; j++)
            {
                data[i][j] = 0;
            }
        }
        cout << "Enter the number of cities-\n";
        cin >> vertices;
        string cities[vertices];
        for (int i = 0; i < vertices; i++)
        {
            string city;
            cout << "Enter the name of the city-\n";
            cin >> cities[i];
        }
        int edges;
        cout << "Enter the number of edges-\n";
        cin >> edges;

        for (int i = 0; i < vertices; i++)
        {
            int fuel;
            for (int j = 0; j < vertices; j++)
            {
                if (i != j)
                {
                    cout << "Enter the amount of fuel required for the journey from city " + cities[i] + " to " << cities[j] << endl; 
                    cin >> fuel;
                    data[i][j] = fuel;
                    pair<string,string> p = make_pair(cities[i], cities[j]);
                    hash[p] = fuel;
                }
                else
                {
                    pair<string,string> p = make_pair(cities[i], cities[j]);
                    hash[p] = 0;
                }
            }
        }
    }

    void display()
    {
        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {
                cout << data[i][j] << " ";
            }
            cout << endl;
        }
    }

    void check_path(pair<string,string> p)
    {
        if (hash[p] != 0)
        {
            cout << "The fuel required from city " << p.first << " to " << p.second << " is " << hash[p] << endl;
        }
        else
        {
            cout << "There is no path from city " << p.first << " to " << p.second << endl;
        }
    }

    void is_connected(int source, vector<bool> &visited)
    {
        visited[source] = true;
        for (int i = 0; i < vertices; i++)
        {
            if (data[source][i] != 0 and visited[i] != true)
            {
                is_connected(i, visited);
            }
        }
    }
};

int main()
{
    Graph g;
    g.read();
    g.display();
    string source, destination;
    cout << "Enter the source city-\n";
    cin >> source;
    cout << "Enter the destination city-\n";
    cin >> destination;
    pair<string,string> p = make_pair(source, destination);
    g.check_path(p);
    vector<bool> visited(MAX, false);
    g.is_connected(0, visited);
    bool flag = true;
    for (int i = 0; i < g.vertices; i++)
    {
        if (visited[i] == false)
        {
            flag = false;
            break;
        }
    }
    if (flag == true)
    {
        cout << "The graph is connected!" << endl;
    }
    else
    {
        cout << "The graph is not connected!" << endl;
    }
    return 0;
}
