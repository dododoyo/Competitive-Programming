import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) 
    {
        int pointer = arr.size()-2;
        int temp = arr.get(arr.size()-1);
        while(pointer >= 0 && arr.get(pointer) > temp)
        {
            arr.set(pointer+1,arr.get(pointer));
            showArray(arr);
            pointer--;
            
        }
        
        arr.set(pointer+1,temp);
        
        showArray(arr);
    }
    public static void showArray(List<Integer> arr)
    {
        for(int i = 0 ; i < arr.size(); i++)
        System.out.print(arr.get(i)+" ");
        System.out.println();
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.insertionSort1(n, arr);

        bufferedReader.close();
    }
}
