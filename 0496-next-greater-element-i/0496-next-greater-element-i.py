class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greatest = []
        hsmap = {}
        
        
        #go through every element of nums2
        for i in nums2:
            foundGreatest = False
            index_of_i = nums2.index(i)
            for j in range(index_of_i+1,len(nums2)):

                if(len(greatest) == 0 and nums2[j] > nums2[index_of_i]):
                    greatest.append(nums2[j])
                    foundGreatest =True
                # elif:
                #     if(greatest[-1] < nums2[j]):
                #         greatest[-1] = nums2[j]
                #         foundGreatest = True

            if foundGreatest:
                hsmap[i] = greatest[-1]
            else:
                hsmap[i] = -1
            greatest = []
        
        #use stack to get the largest element - for each element
        
        #map all elements with their respective larger element
        
        #copy all larger for nums in num1
        
        for i in range(len(nums1)):
            nums1[i] = hsmap[nums1[i]]
            
        return nums1

        
                

                    
        
        
                