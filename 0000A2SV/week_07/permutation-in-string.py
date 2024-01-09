class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = self.freq(s1)
        for right in range(len(s2)-len(s1)+1):
            if self.freq(s2[right:right+len(s1)]) == s1_freq:
                return True
        return False

    def freq(self,s2):
        s2_freq,off_set = [0]*26,ord("a")
        for char in s2:s2_freq[ord(char) - off_set] += 1
        return s2_freq
        