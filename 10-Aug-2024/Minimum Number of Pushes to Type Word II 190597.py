# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        track = [0 for _ in range(26)]

        for char in word:
            index = ord(char) - 97
            track[index] += 1
        
        track.sort(reverse = True)

        for i in range(8,26):
            if i > 23:
                track[i] *= 4
            elif i > 15:
                track[i] *= 3
            elif i > 7:
                track[i] *= 2
        solution = sum(track)
        return solution


        