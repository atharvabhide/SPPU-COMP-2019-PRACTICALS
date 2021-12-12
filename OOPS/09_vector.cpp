#include<bits/stdc++.h>
using namespace std;
void display(vector<int> &v)
{
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}
int main()
{
    vector<int> v;
    cout << "Initial size of the vector is- " << v.size() << endl;
    int n;
    cout << "Enter the number of elements you want in the vector-\n";
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int element;
        cout << "Enter the vector element-\n";
        cin >> element;
        v.push_back(element);
    }
    cout << "Size after insertion is- " << v.size() << endl;
    cout << "Capacity after insertion is- " << v.capacity() << endl;
    cout << "The vector elements are-\n";
    display(v);

    cout << "Enter the element to be inserted at the end of the vector-\n";
    int y;
    cin >> y;
    v.push_back(y);
    cout << "The vector elements after insertion are-\n";
    display(v);

    cout << "Enter the element to inserted in the vector-\n";
    int x;
    cin >> x;
    cout << "Enter position at which the element is to be inserted in the vector-\n";
    int position;
    cin >> position;
    vector<int> :: iterator it = v.begin();
    advance(it, position);
    v.insert(it,x);
    cout << "The vector elements after insertion are-\n";
    display(v);

    v.pop_back();
    cout << "The vector elements after removing the last element are-\n";
    display(v);

    int start;
    int end;
    cout << "Enter the starting position from where the elements are to be deleted-\n";
    cin >> start;
    cout << "Enter the ending position-\n";
    cin >> end;
    auto it1 = next(v.begin(),start);
    auto it2 = next(v.begin(),end);
    v.erase(it1,it2);
    cout << "The vector elements after erasing the given range of elements are-\n";
    display(v);
}
