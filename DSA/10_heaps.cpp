#include<bits/stdc++.h>
using namespace std;

struct MinHeap
{
    int* arr;
    int capacity;
    int size;

    MinHeap(int capacity)
    {
        this->capacity = capacity;
        size = 0;
        arr = new int(capacity);
    }

    int left(int i)
    {
        return (2*i+1);
    }

    int right(int i)
    {
        return (2*i+2);
    }

    int parent(int i)
    {
        return ((i-1)/2);
    }

    void insert(int marks)
    {
        if (size == capacity)
        {
            cout << "Overflow" << endl;
            return;
        }
        size++;
        arr[size-1] = marks;
        
        int i = size-1;
        while (i != 0 and arr[parent(i)] > arr[i])
        {
            swap(arr[i], arr[parent(i)]);
            i = parent(i);
        }
    }
};

struct MaxHeap
{
    int* arr;
    int capacity;
    int size;

    MaxHeap(int capacity)
    {
        this->capacity = capacity;
        arr = new int(capacity);
        size = 0;
    }

    int left(int i)
    {
        return (2*i+1);
    }

    int right(int i)
    {
        return (2*i+2);
    }

    int parent(int i)
    {
        return ((i-1)/2);
    }

    void insert(int marks)
    {
        if (size == capacity)
        {
            return;
        }
        size++;
        arr[size-1] = marks;
        int i = size-1;
        while (i != 0 and arr[parent(i)] < arr[i])
        {
            swap(arr[parent(i)], arr[i]);
            i = parent(i);
        }
    }
};

int main()
{
    int n;
    cout << "Enter the number of students-\n";
    cin >> n;
    MinHeap min_heap(n);
    MaxHeap max_heap(n);
    for (int i = 0; i < n; i++)
    {
        int marks;
        cout << "Enter the marks of the student-\n";
        cin >> marks;
        min_heap.insert(marks);
        max_heap.insert(marks);
    }

    cout << "The minimum marks are- " << min_heap.arr[0] << endl;
    cout << "The maximum marks are- " << max_heap.arr[0] << endl;
}
