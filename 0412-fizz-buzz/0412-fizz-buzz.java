class Solution {
    public List<String> fizzBuzz(int n) 
    {
      List<String> solution = Arrays.asList(new String[n]);      
        for(int i = 1 ; i < n+1 ; i++)
        {
            if(i%15 == 0)
            solution.set(i-1,"FizzBuzz");
            else if(i%5 == 0)
            solution.set(i-1,"Buzz");
            else if(i%3 == 0)
            solution.set(i-1,"Fizz");
            else
            solution.set(i-1,String.valueOf(i));
        }
        return solution;
        
    }
}