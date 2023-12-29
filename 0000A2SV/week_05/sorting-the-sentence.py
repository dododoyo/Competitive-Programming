class Solution:
    def sortSentence(self, s: str) -> str:
        s_list = s.split(" ")
        s_list.sort(key= lambda x: x[-1])
        solution = [i[:-1] for i in s_list]
        return " ".join(solution)