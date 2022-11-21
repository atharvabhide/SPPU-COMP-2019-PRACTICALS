import java.util.*;
import java.io.*;

public class Pass2 
{
    ArrayList<TableRow> SYMTAB, LITTAB;    

    public Pass2()
    {
        SYMTAB = new ArrayList<>();
        LITTAB = new ArrayList<>();
    }

    public static void main(String[] args) throws Exception
    {
        Pass2 pass2 = new Pass2();
        pass2.generateCode("IC.txt");    
    }

    public void readTables() throws Exception
    {
        BufferedReader br;
        String line;

        br = new BufferedReader(new FileReader("SYMTAB.txt"));
        while((line=br.readLine()) != null)
        {
            String parts[] = line.split("\\s+");
            SYMTAB.add(new TableRow(parts[1], Integer.parseInt(parts[2]), Integer.parseInt(parts[0])));
        }
        br.close();

        br = new BufferedReader(new FileReader("LITTAB.txt"));
        while((line=br.readLine()) != null)
        {
            String parts[] = line.split("\\s+");
            LITTAB.add(new TableRow(parts[1], Integer.parseInt(parts[2]), Integer.parseInt(parts[0])));
        }
        br.close();
    }

    public void generateCode(String filename) throws Exception
    {   
        readTables();
        BufferedReader br = new BufferedReader(new FileReader(filename));
        BufferedWriter bw = new BufferedWriter(new FileWriter("PASS2.txt"));
        String line,code;

        while((line=br.readLine()) != null)
        {
            String parts[] = line.split("\\s+");
            if (parts[0].contains("AD") || parts[0].contains("DL,02"))
            {
                bw.write("\n");
                continue;
            }
            else if (parts.length == 2)
            {
                if (parts[0].contains("DL"))
                {
                    int constant = Integer.parseInt(parts[1].replaceAll("[^0-9]", ""));
                    code = "00\t0\t" + String.format("%03d", constant) + "\n";
                    bw.write(code);
                }
                else if (parts[0].contains("IS"))
                {
                    int opcode = Integer.parseInt(parts[0].replaceAll("[^0-9]", ""));
                    int symIndex = Integer.parseInt(parts[1].replaceAll("[^0-9]", ""));

                    if (parts[1].contains("S"))
                    {
                        code = String.format("%02d", opcode) + "\t0\t" + String.format("%03d", SYMTAB.get(symIndex-1).getAddress()) + "\n";
                        bw.write(code);
                    }
                    else if (parts[1].contains("L"))
                    {
                        code = String.format("%02d", opcode) + "\t0\t" + String.format("%03d", LITTAB.get(symIndex-1).getAddress()) + "\n";
                        bw.write(code);
                    }
                }
            }
            else if (parts.length == 1 && parts[0].contains("IS"))
            {
                int opcode = Integer.parseInt(parts[0].replaceAll("[^0-9]", ""));
                code = String.format("%02d", opcode) + "\t0\t" + String.format("%03d", 0) + "\n";
                bw.write(code);
            }
            else if (parts.length == 3 && parts[0].contains("IS"))
            {
                int opcode = Integer.parseInt(parts[0].replaceAll("[^0-9]", ""));
                int regcode = Integer.parseInt(parts[1]);
                int symIndex = Integer.parseInt(parts[2].replaceAll("[^0-9]", ""));

                if (parts[2].contains("S"))
                {
                    code = String.format("%02d", opcode) + "\t" + regcode + "\t" + String.format("%03d", SYMTAB.get(symIndex-1).getAddress()) + "\n";
                    bw.write(code);
                }
                else if (parts[2].contains("L"))
                {
                    code = String.format("%02d", opcode) + "\t" + regcode + "\t" + String.format("%03d", LITTAB.get(symIndex-1).getAddress()) + "\n";
                    bw.write(code);
                }
            }
        }
        br.close();
        bw.close();
    }
}
