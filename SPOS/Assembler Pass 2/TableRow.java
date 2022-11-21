public class TableRow 
{
    String symbol;
    int address;
    int index;
    
    public TableRow(String symbol, int address)
    {
        this.symbol = symbol;
        this.address = address;
    }

    public TableRow(String symbol, int address, int index)
    {
        this.symbol = symbol;
        this.address = address;
        this.index = index;
    }

    public void setSymbol(String symbol)
    {
        this.symbol = symbol;
    }

    public void setAddress(int address)
    {
        this.address = address;
    }

    public void setIndex(int index)
    {
        this.index = index;
    }

    public String getSymbol()
    {
        return symbol;
    }

    public int getAddress()
    {
        return address;
    }

    public int getIndex()
    {
        return index;
    }
}
