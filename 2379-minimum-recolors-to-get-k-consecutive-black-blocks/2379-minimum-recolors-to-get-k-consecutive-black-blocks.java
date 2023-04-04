class Solution {
    public int minimumRecolors(String blocks, int k) 
    {
        //let's use two pointers
        int swaps = 0;
        for(int i = 0 ; i < k ; i++){if(blocks.charAt(i) == 'W')swaps++;}
        int currentSwaps = swaps;
        for(int i = 0, j = k; j < blocks.length();i++,j++)
        {
            if(blocks.charAt(i)=='W' && blocks.charAt(j)=='B')currentSwaps--;
            else if(blocks.charAt(i)=='B' && blocks.charAt(j) == 'W')currentSwaps++;
            swaps = Math.min(swaps,currentSwaps);
        }
        return swaps;
        
    }
}