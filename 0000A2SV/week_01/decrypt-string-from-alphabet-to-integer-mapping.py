class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        solution = []
        while i < len(s)-2:
            if s[i+2] == "#":
                solution.append(chr(int(s[i:i+2])+96))
                i += 3
            else:
                solution.append(chr(int(s[i])+96))
                i += 1
        while i < len(s):
            solution.append(chr(int(s[i])+96))
            i += 1
        return "".join(solution)

        