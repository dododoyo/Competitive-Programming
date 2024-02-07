class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0]*(len(s)+1)
        for shift in shifts:
            prefix_sum[shift[0]] += 1 if shift[2] == 1 else -1
            prefix_sum[shift[1]+1] += -1 if shift[2] == 1 else 1

        solution = [""]*len(s)
        accumulator = 0
        for i in range(len(s)):
            accumulator += prefix_sum[i]
            solution[i] = chr(((ord(s[i]) + accumulator) - 97) % 26 + 97)
        return "".join(solution)