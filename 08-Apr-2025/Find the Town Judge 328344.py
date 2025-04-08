# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # remove offset by one
        trust = [(a-1,b-1) for a,b in trust]

        person_trusts = [[] for _ in range(n)]
        person_trusted_by = [[] for _ in range(n)]

        for a,b in trust:
            person_trusted_by[b].append(a)
            person_trusts[a].append(b)

        # check conditions
        valid = [0,0]
        for i in range(n):
            # trusts no one 
            trusts_no_one = person_trusts[i] == []

            # trusted by eveyone 
            trusted_by_all = len(person_trusted_by[i]) == n-1

            if trusts_no_one and trusted_by_all:
                valid[0] += 1
                valid[1] = i

        if valid[0] == 1:
            return valid[1] + 1
        else:
            return -1

