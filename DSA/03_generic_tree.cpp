#include<bits/stdc++.h>
using namespace std;

struct Node
{
    string name;
    vector<Node*> nodes;
    Node (string name)
    {
        this->name = name;
    }
};

Node* construct()
{
    string rootData;
    cout << "Enter the name here-\n";
    cin >> rootData;
    Node* root = new Node(rootData);

    int n;
    cout << "Enter the number of children-\n";
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        Node* child = construct();
        root->nodes.push_back(child);
    }

    return root;
}

void display(Node* root)
{
    if (root == NULL)
    {
        return;
    }
    cout << root->name << " : ";
    for (int i = 0; i < root->nodes.size(); i++)
    {
        cout << root->nodes[i]->name << " ";
    }
    cout << endl;
    for (int i = 0; i < root->nodes.size(); i++)
    {
        display(root->nodes[i]);
    }
}

int main()
{
    Node* book = construct();
    display(book);
    return 0;
}
