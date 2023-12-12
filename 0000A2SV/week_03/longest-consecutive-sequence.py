class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen_dict = {}
        for number in nums:
            seen_dict[number] = False
        longest_length = 0
        
        for number in nums:
            current_length = 1
            next_number = number + 1 
            
            while (next_number in seen_dict) and seen_dict[next_number] == False:
                current_length += 1
                seen_dict[next_number] = True
                next_number += 1
                
            previous_number = number - 1
            
            while (previous_number in seen_dict) and seen_dict[previous_number] == False:
                current_length += 1
                seen_dict[previous_number] = True
                previous_number -= 1
            longest_length = max(longest_length,current_length)
        return longest_length
                
            
        