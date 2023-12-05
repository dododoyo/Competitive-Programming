class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set(["q","w","e","r","t","y","u","i","o","p"])
        second_row = set(["a","s","d","f","g","h","j","k","l"])
        third_row = set(['z','x','c','v','b','n','m'])
        solution = []
        for each_word in words:
            word_as_set = set(each_word.lower())
            # if intersection is equal to the set that means all 
            # of the characters in the word are in the set 
            # so we can say they lie on the same row 
            intersection_with_first_row = first_row&word_as_set
            intersection_with_second_row = second_row&word_as_set
            intersection_with_third_row = third_row&word_as_set
            if (intersection_with_first_row == word_as_set) or (intersection_with_second_row == word_as_set) or (intersection_with_third_row == word_as_set):
                solution.append(each_word);
        return solution