/*
 * @lc app=leetcode id=1512 lang=java
 *
 * [1512] Number of Good Pairs
 */

// @lc code=start
import java.util.HashMap;
class Solution {
    public int numIdenticalPairs(int[] nums) {

    HashMap<Integer,Integer>mp=new HashMap<>();

    int count=0;

    for(int val : nums)
    {

        if(!mp.containsKey(val))
        {
            mp.put(val,1);
        }
        else
        {
            count+=mp.get(val);
            mp.put(val,mp.get(val)+1);
        }

    }

    return count;

    }
}
// @lc code=end

