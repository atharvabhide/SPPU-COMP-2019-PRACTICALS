import java.util.*;

public class priority
{
    public static void main(String[] args) throws Exception
    {
        // input processes with burst time and priority
        Scanner scan = new Scanner(System.in);
        
        System.out.println("Enter the number of processes-");
        int processes = scan.nextInt();

        int[] bt = new int[processes];
        int[] priorities = new int[processes];

        System.out.println("Enter the burst times-");
        for (int i = 0; i < processes; i++)
        {
            bt[i] = scan.nextInt();
        }

        System.out.println("Enter the priorites-");
        for (int i = 0; i < processes; i++)
        {
            priorities[i] = scan.nextInt();
        }

        // sort burst times according to priority (low numeric value -> high priority)
        Map<Integer,Integer> mp = new TreeMap<>();
        for (int i = 0; i < processes; i++)
        {
            mp.put(priorities[i], bt[i]);
        }

        int[] finalbts = new int[processes];
        int x = 0;
        for (Map.Entry<Integer,Integer> e : mp.entrySet())
        {
            finalbts[x] = e.getValue();
            x++;
        }
        scan.close();

        // apply fcfs
        int wt[] = new int[processes];
        int tt[] = new int[processes];
        wt[0] = 0;
        
        for (int i = 1; i < processes; i++)
        {
            wt[i] = wt[i-1] + bt[i-1];
        }

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
    }
}
