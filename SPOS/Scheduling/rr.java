import java.util.*;

public class rr 
{   
    public static void main(String[] args) throws Exception
    {
        // algo -> gfg
        Scanner scan = new Scanner(System.in);    

        System.out.println("Enter the number of processes-");
        int processes = scan.nextInt();

        System.out.println("Enter the quantum here-");
        int quantum = scan.nextInt();

        int[] bt = SchedulingUtils.readBurstTimes(scan, processes);

        int[] rem_bt = new int[processes];
        for (int i = 0; i < processes; i++)
        {
            rem_bt[i] = bt[i];
        }

        int[] wt = new int[processes];
        for (int i = 0; i < processes; i++)
        {
            wt[i] = 0;
        }

        int t = 0;
        
        while(true)
        {
            boolean done = true;
            for (int i = 0; i < processes; i++)
            {
                if (rem_bt[i] > 0)
                {
                    done = false;
                    if (rem_bt[i] > quantum)
                    {
                        t += quantum;
                        rem_bt[i] -= quantum;
                    }
                    else
                    {
                        t += rem_bt[i];
                        wt[i] = t - bt[i];
                        rem_bt[i] = 0;
                    }
                }
            }
            if (done == true)
            {
                break;
            }
        }

        int[] tt = SchedulingUtils.calculateTurnaroundTimes(wt, bt);

        System.out.println("Final outputs are-");
        SchedulingUtils.printAverages(wt, tt, processes);

        scan.close();
    }
}
