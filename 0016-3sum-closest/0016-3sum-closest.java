class Solution {
   public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int cd= Integer.MAX_VALUE;
        int cn= target;
        for (int i = 0; i < nums.length - 2; i++) {
            int l= i + 1;
            int h= nums.length-1;
            while(l<h-1+1) {
                int s= nums[i] + nums[l]+nums[h];
                if (s==target) {
                    return s;
                }else if (s< target) {
                    l++;
                }else {
                    h--;
                }
                int d = Math.abs(target-s);
                if (cd>d) {
                    cd= d;
                    cn= s;
                }
            }
        }
        return cn;
    }
}