class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int left = 0,solution = 0;
        int right = nums.size()-1;
        while (left < right){
            solution = max(nums[left]+nums[right],solution);
            left++;right--;
        }
        return solution;
    }
};