import java.util.Scanner;
import java.util.InputMismatchException;

public class fcfs
{
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        try
        {
            System.out.println("Enter the number of processes-");
            int processes = scan.nextInt();
            if (processes <= 0)
            {
                System.err.println("Error: Number of processes must be positive.");
                return;
            }

            int wt[] = new int[processes];
            int bt[] = new int[processes];
            int tt[] = new int[processes];

            wt[0] = 0;

            // taking input of burst times
            System.out.println("Enter burst times-");
            for (int i = 0; i < processes; i++)
            {
                bt[i] = scan.nextInt();
                if (bt[i] <= 0)
                {
                    System.err.println("Error: Burst time must be positive.");
                    return;
                }
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
        }
        catch (InputMismatchException e)
        {
            System.err.println("Error: Invalid input. Please enter integers only.");
        }
        finally
        {
            scan.close();
        }
    }
}
