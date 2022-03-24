#include<bits/stdc++.h>
using namespace std;
#define MAX 100

struct Graph
{
    int data[MAX][MAX];
    int vertices;
    int edges;

    void read()
    {
        cout << "Enter the number of vertices in the graph-\n";
        cin >> vertices;

        for (int i = 0; i < vertices; i++)
        {
            for (int j = 0; j < vertices; j++)
            {
                if (i != j)
                {
                    cout << "Enter the weight between vertex " + to_string(i) + " and " + to_string(j) + "\n";
                    cin >> data[i][j];
                }
                else
                {
                    data[i][j] = 0;
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

    int minKey(int key[], bool mstSet[])
    {
        int min = INT_MAX, min_index;
        for (int v = 0; v < vertices; v++)
        {
            if (mstSet[v] == false && key[v] < min)
            {
                min = key[v], min_index = v;
            }
        }
        return min_index;
    }

    void printMST(int parent[])
    {
        int cost = 0;
        cout<<"Edge \tWeight\n";
        for (int i = 1; i < vertices; i++)
        {
            cout<< parent[i] <<" - "<<i<<" \t"<< data[i][parent[i]] <<" \n";
        }
        for (int i = 1; i < vertices; i++)
        {
            cost += data[i][parent[i]];
        }
        cout << cost << endl;
    }

    void primMST()
    {
        int parent[vertices];
        int key[vertices];
        bool mstSet[vertices];
 
        for (int i = 0; i < vertices; i++)
        {
            key[i] = INT_MAX, mstSet[i] = false;
        }
        key[0] = 0;
        parent[0] = -1;
        for (int count = 0; count < vertices - 1; count++)
        {
            int u = minKey(key, mstSet);
            mstSet[u] = true;
            for (int v = 0; v < vertices; v++)
            {
                if (data[u][v] && mstSet[v] == false && data[u][v] < key[v])
                {
                    parent[v] = u, key[v] = data[u][v];
                }
            }
        }
        printMST(parent);
    }
};

int main()
{
    Graph g;
    g.read();
    g.display();
    g.primMST();
    return 0;
}
