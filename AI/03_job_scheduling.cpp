// Program to find the maximum profit job sequence from a given array 
// of jobs with deadlines and profits 
#include<bits/stdc++.h>
using namespace std; 

// A structure to represent a job 
struct Job 
{ 
    int id;	 // Job Id 
    int dead; // Deadline of job 
    int profit; // Profit if job is over before or on deadline 
}; 

class Solution 
{
    public:
    //Function to find the maximum profit and the number of jobs done.
    
    static bool cmp(Job a, Job b)
    {
        if (a.profit > b.profit)
        {
            return true;
        }
        return false;
    }
    
    vector<int> JobScheduling(Job arr[], int n) 
    { 
        sort(arr, arr+n, cmp);
        int max_deadline = INT_MIN;
        for (int i = 0; i < n; i++)
        {
            if (arr[i].dead > max_deadline)
            {
                max_deadline = arr[i].dead;
            }
        }
        vector<int> gantt_chart(max_deadline+1, -1);
        int profit = 0;
        int jobs = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = arr[i].dead; j > 0; j--)
            {
                if (gantt_chart[j] == -1)
                {
                    gantt_chart[j] = arr[i].id;
                    jobs++;
                    profit += arr[i].profit;
                    break;
                }
            }
        }
        vector<int> res = {jobs, profit};
        return res;
    } 
};

// Driver program to test methods 
int main() 
{ 
    int t;
    //testcases
    cin >> t;
    
    while(t--){
        int n;
        
        //size of array
        cin >> n;
        Job arr[n];
        
        //adding id, deadline, profit
        for(int i = 0;i<n;i++){
                int x, y, z;
                cin >> x >> y >> z;
                arr[i].id = x;
                arr[i].dead = y;
                arr[i].profit = z;
        }
        Solution ob;
        //function call
        vector<int> ans = ob.JobScheduling(arr, n);
        cout<<ans[0]<<" "<<ans[1]<<endl;
    }
	return 0; 
}
