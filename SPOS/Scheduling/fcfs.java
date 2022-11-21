import java.util.Scanner;

public class fcfs
{
    public static void main(String[] args) throws Exception
    {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the number of processes-");
        int processes = scan.nextInt();

        int wt[] = new int[processes];
        int bt[] = new int[processes];
        int tt[] = new int[processes];

        wt[0] = 0;

        // taking input of burst times
        System.out.println("Enter burst times-");
        for (int i = 0; i < processes; i++)
        {
            bt[i] = scan.nextInt();
        }

        // finding the waiting times
        for (int i = 1; i < processes; i++)
        {
            wt[i] = bt[i-1] + wt[i-1];
        }

        // finding the turnaround times
        for (int i = 0; i < processes; i++)
        {
            tt[i] = wt[i] + bt[i];
        }

        // final output
        float total_wt = 0;
        float total_tt = 0;
        for (int i = 0; i < processes; i++)
        {
            total_wt += wt[i];
            total_tt += tt[i];
        }
        System.out.println("Average waiting time and Average turnaround time respectively-");
        System.out.println(total_wt/processes);
        System.out.println(total_tt/processes);

        scan.close();
    }
}
