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

    public static void main(String[] args)
    {
        Pass2 pass2 = new Pass2();
        try {
            pass2.generateCode("IC.txt");
        } catch (FileNotFoundException e) {
            System.err.println("Error: Required input file not found. " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Error: Invalid number format in input file. " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error during code generation: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public void readTables() throws IOException
    {
        String line;

        try (BufferedReader br = new BufferedReader(new FileReader("SYMTAB.txt")))
        {
            while((line=br.readLine()) != null)
            {
                String parts[] = line.split("\\s+");
                if (parts.length < 3) {
                    throw new IOException("Invalid SYMTAB format: expected 3 columns, got " + parts.length);
                }
                SYMTAB.add(new TableRow(parts[1], Integer.parseInt(parts[2]), Integer.parseInt(parts[0])));
            }
        }

        try (BufferedReader br = new BufferedReader(new FileReader("LITTAB.txt")))
        {
            while((line=br.readLine()) != null)
            {
                String parts[] = line.split("\\s+");
                if (parts.length < 3) {
                    throw new IOException("Invalid LITTAB format: expected 3 columns, got " + parts.length);
                }
                LITTAB.add(new TableRow(parts[1], Integer.parseInt(parts[2]), Integer.parseInt(parts[0])));
            }
        }
    }

    public void generateCode(String filename) throws IOException
    {   
        readTables();

        try (BufferedReader br = new BufferedReader(new FileReader(filename));
             BufferedWriter bw = new BufferedWriter(new FileWriter("PASS2.txt")))
        {
            String line, code;

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

                        if (symIndex < 1) {
                            throw new IOException("Invalid symbol index: " + symIndex);
                        }

                        if (parts[1].contains("S"))
                        {
                            if (symIndex > SYMTAB.size()) {
                                throw new IOException("Symbol index " + symIndex + " out of bounds (SYMTAB size: " + SYMTAB.size() + ")");
                            }
                            code = String.format("%02d", opcode) + "\t0\t" + String.format("%03d", SYMTAB.get(symIndex-1).getAddress()) + "\n";
                            bw.write(code);
                        }
                        else if (parts[1].contains("L"))
                        {
                            if (symIndex > LITTAB.size()) {
                                throw new IOException("Literal index " + symIndex + " out of bounds (LITTAB size: " + LITTAB.size() + ")");
                            }
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

                    if (symIndex < 1) {
                        throw new IOException("Invalid symbol index: " + symIndex);
                    }

                    if (parts[2].contains("S"))
                    {
                        if (symIndex > SYMTAB.size()) {
                            throw new IOException("Symbol index " + symIndex + " out of bounds (SYMTAB size: " + SYMTAB.size() + ")");
                        }
                        code = String.format("%02d", opcode) + "\t" + regcode + "\t" + String.format("%03d", SYMTAB.get(symIndex-1).getAddress()) + "\n";
                        bw.write(code);
                    }
                    else if (parts[2].contains("L"))
                    {
                        if (symIndex > LITTAB.size()) {
                            throw new IOException("Literal index " + symIndex + " out of bounds (LITTAB size: " + LITTAB.size() + ")");
                        }
                        code = String.format("%02d", opcode) + "\t" + regcode + "\t" + String.format("%03d", LITTAB.get(symIndex-1).getAddress()) + "\n";
                        bw.write(code);
                    }
                }
            }
        }
    }
}
