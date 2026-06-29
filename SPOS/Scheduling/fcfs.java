import java.util.Scanner;

public class fcfs
{
    public static void main(String[] args) throws Exception
    {
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the number of processes-");
        int processes = scan.nextInt();

        int[] bt = SchedulingUtils.readBurstTimes(scan, processes);

        int wt[] = new int[processes];
        wt[0] = 0;

        // finding the waiting times
        for (int i = 1; i < processes; i++)
        {
            wt[i] = bt[i-1] + wt[i-1];
        }

        // finding the turnaround times
        int[] tt = SchedulingUtils.calculateTurnaroundTimes(wt, bt);

        // final output
        SchedulingUtils.printAverages(wt, tt, processes);

        scan.close();
    }
}
