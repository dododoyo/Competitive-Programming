class Solution:
    def compress(self, chars: List[str]) -> int:
        edit_pointer = 0
        right = 1
        curr_freq = 1
        while right < len(chars):
            if chars[right] != chars[right-1]:
                chars[edit_pointer] = chars[right-1]
                edit_pointer += 1
                if curr_freq > 1:
                    for i in str(curr_freq):
                        chars[edit_pointer] = i
                        edit_pointer += 1  
                curr_freq = 1
            
            else:
                curr_freq += 1
            right += 1
        chars[edit_pointer] = chars[right-1]
        edit_pointer += 1
        if curr_freq > 1:
            for i in str(curr_freq):
                chars[edit_pointer] = i
                edit_pointer += 1  
        curr_freq = 1
    
        return edit_pointer
                