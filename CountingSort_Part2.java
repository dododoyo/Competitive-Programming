public class CountingSort_Part2 
{import java.io.*;
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
         * Complete the 'countingSort' function below.
         *
         * The function is expected to return an INTEGER_ARRAY.
         * The function accepts INTEGER_ARRAY arr as parameter.
         */
    
        public static List<Integer> countingSort(List<Integer> arr) 
        {
            int maxElement = Collections.max(arr);
            
            int[] array1 = new int[maxElement+1];
            
            for( int i = 0 ; i < arr.size() ; i++)
            {
                array1[arr.get(i)]++;
            }
            
            for ( int i = 1 ; i < array1.length ; i++)
            {
                array1[i] = array1[i] + array1[i-1];
            }
            
            int[] array2 = new int[arr.size()];
            
            for (int i = (arr.size() - 1); i > -1 ; i--)
            {
                array2[--array1[arr.get(i)]] = arr.get(i);
            }
            
            for ( int i = 0 ; i < arr.size() ; i++)
            arr.set(i, array2[i]);
            
            return arr;
        }
    
    }
    
    public class Solution {
        public static void main(String[] args) throws IOException {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));
    
            int n = Integer.parseInt(bufferedReader.readLine().trim());
    
            List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());
    
            List<Integer> result = Result.countingSort(arr);
    
            bufferedWriter.write(
                result.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
                + "\n"
            );
    
            bufferedReader.close();
            bufferedWriter.close();
        }
    }
    
    
}
