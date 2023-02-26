class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length_ = len(nums)
        solution = []
        #let's use two pointers
        
        nums.sort()
        
        for i in range(length_):
            
            #if current element is dupicated no need for iteration
            if((i>0) and (nums[i]==nums[i-1])):
                continue
                
            p1 = i+1
            p2 = length_ - 1
            
            while(p1 < p2):
                # if the elements satisfy the condition append them to the solution
                if(nums[i] + nums[p1] + nums[p2] == 0):
                    solution.append([nums[i],nums[p1],nums[p2]])
                    
                    #to remove duplicates
                    while((p1<p2) and (nums[p1+1]==nums[p1])):
                        p1 += 1
                    while((p1<p2) and (nums[p2-1]==nums[p2])):
                        p2 -= 1
                    p1 += 1
                    p2 -= 1
                elif(nums[i] + nums[p1] + nums[p2] > 0):
                    p2 -= 1 
                else:
                    p1 += 1
        return solution
            
            
            