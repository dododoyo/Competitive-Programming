class Solution:
    def balancedString(self, s: str) -> int:
        # string only has [Q,W,E,R]
        chars,n = ["Q","W","E","R"],len(s)
        target,freq = n//4,defaultdict(int)

        # store each character's frequency
        for i in range(n):freq[s[i]] += 1
            
        min_len,left = n,0
        # the freq dict will now be responsible 
        # for counting frequency of elements outside our window
        for right in range(n):
            """ when a character is in our sliding(inside) window
            it is no longer part of our outside window
            so we decrease it's frequency from our outside window
            """
            freq[s[right]] -= 1
            while all(freq[char] <= target for char in chars) and (left < n):
                min_len = min(min_len,right-left+1)
                freq[s[left]] += 1
                left += 1
        return min_len

        