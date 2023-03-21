class Solution:
    def sortSentence(self, s: str) -> str:
        sen_list = s.split()
        ord_sen = [""]*len(sen_list)
        for i in sen_list:
            ord_sen[int(i[-1])-1] = i[:-1]
        return " ".join(ord_sen)