import java.util.*;
public class TheatreSquare
{
    public static void main(String[] args)
    {
        Scanner kb  = new Scanner(System.in);
        double n = Double.parseDouble(kb.next());
        double m = Double.parseDouble(kb.next());
        double a = Double.parseDouble(kb.next());
        kb.close();
        
        double total = Math.ceil(n/a)*Math.ceil(m/a);
        System.out.println((long)total);
    
    }
    
}