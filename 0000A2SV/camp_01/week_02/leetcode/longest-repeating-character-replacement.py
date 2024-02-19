class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        freq_arr = [0]*26
        offset,max_len = 65,0
        """
        for each window get characters to be replaced
        if replaced > k decrease window with left
        else register current window"""
        while right < len(s):
            freq_arr[ord(s[right])-offset] += 1
            # get the number of characters to be replaced
            window_length = right-left+1
            longest_same = max(freq_arr)
            # characters replaced are ones besides the most frequent occuring
            replaced = window_length - longest_same
            if replaced > k:
                freq_arr[ord(s[left])-offset] -= 1
                left += 1
            else:
                max_len = max(max_len,window_length)
            right += 1
        return max_len