#include <iostream>
#include <vector>
#include <omp.h>

using namespace std;

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped = true;

    while (swapped) {
        swapped = false;
        #pragma omp parallel for
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                swap(arr[i], arr[i + 1]);
                swapped = true;
            }
        }
    }
}

void merge(vector<int>& arr, int l, int m, int r) {
    vector<int> temp;
    int left = l;
    int right = m + 1;

    while (left <= m && right <= r) {
        if (arr[left] <= arr[right]) {
            temp.push_back(arr[left]);
            left++;
        }
        else {
            temp.push_back(arr[right]);
            right++;
        }
    }

    while (left <= m) {
        temp.push_back(arr[left]);
        left++;
    }

    while (right <= r) {
        temp.push_back(arr[right]);
        right++;
    }

    for (int i = l; i <= r; i++) {
        arr[i] = temp[i - l];
    }
}

void mergeSort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        #pragma omp parallel sections
        {
            #pragma omp section
            mergeSort(arr, l, m);
            #pragma omp section
            mergeSort(arr, m + 1, r);
        }
        merge(arr, l, m, r);
    }
}

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    bubbleSort(arr);
    cout << "Sorted array using Bubble Sort: ";
    for (int num : arr)
        cout << num << " ";
    cout << endl;

    mergeSort(arr, 0, n - 1);
    cout << "Sorted array using Merge Sort: ";
    for (int num : arr)
        cout << num << " ";
    cout << endl;

    return 0;
}
