class Solution:
    def printVertically(self, s: str) -> List[str]:
        words_list = s.split(' ')
        maximum_length = 0
        for word in words_list:
            maximum_length = max(maximum_length,len(word));
        for i in range(len(words_list)):
            words_list[i] = words_list[i] + " "*(maximum_length-len(words_list[i]))
        solution = [""]*maximum_length
        for i in range(maximum_length):
            each_word = []
            for word in words_list:
                each_word.append(word[i])
            while each_word[-1] == " ":
                each_word.pop();
            solution[i] = "".join(each_word);
        return solution
        