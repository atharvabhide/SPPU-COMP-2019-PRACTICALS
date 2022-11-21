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

        int[] bt = new int[processes];

        System.out.println("Enter the burst times here-");
        for (int i = 0; i < processes; i++)
        {
            bt[i] = scan.nextInt();
        }

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

        int[] tt = new int[processes];
        for (int i = 0; i < processes; i++)
        {
            tt[i] = wt[i] + bt[i];
        }

        float total_wt = 0;
        float total_tt = 0;
        for (int i = 0; i < processes; i++)
        {
            total_wt += wt[i];
            total_tt += tt[i];
        }

        System.out.println("Final outputs are-");
        System.out.println(total_wt/processes);
        System.out.println(total_tt/processes);

        scan.close();
    }
}
