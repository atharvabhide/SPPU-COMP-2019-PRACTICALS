import java.util.Scanner;

/**
 * Shared utilities for CPU scheduling algorithm practicals.
 */
public class SchedulingUtils
{
    /** Read burst times for the given number of processes. */
    public static int[] readBurstTimes(Scanner scan, int processes)
    {
        int[] bt = new int[processes];
        System.out.println("Enter the burst times-");
        for (int i = 0; i < processes; i++)
        {
            bt[i] = scan.nextInt();
        }
        return bt;
    }

    /** Compute turnaround times from waiting times and burst times. */
    public static int[] calculateTurnaroundTimes(int[] wt, int[] bt)
    {
        int[] tt = new int[wt.length];
        for (int i = 0; i < wt.length; i++)
        {
            tt[i] = wt[i] + bt[i];
        }
        return tt;
    }

    /** Print average waiting time and average turnaround time. */
    public static void printAverages(int[] wt, int[] tt, int processes)
    {
        float total_wt = 0;
        float total_tt = 0;
        for (int i = 0; i < processes; i++)
        {
            total_wt += wt[i];
            total_tt += tt[i];
        }
        System.out.println("Average waiting time and Average turnaround time respectively-");
        System.out.println(total_wt / processes);
        System.out.println(total_tt / processes);
    }
}
