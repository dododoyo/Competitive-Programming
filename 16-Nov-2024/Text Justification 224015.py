# Problem: Text Justification - https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        solution = []
        current_words = []
        current_line_length = 0

        n = len(words)

        for i in range(n):
            current_word = words[i]

            # current word can't be added to the running line 
            if current_line_length + len(current_words) + len(current_word) > maxWidth:
                # get all the available spaces
                available_space = maxWidth - current_line_length

                # for n words we will have n-1 space in between words
                between_words = max(1,len(current_words)-1)

                space = available_space//between_words

                # remaining space will be added to each word starting from the first
                remaining_space = available_space%between_words

                for j in range(between_words):
                    current_words[j] += " "*space
                    if remaining_space:
                        current_words[j] += " "
                        remaining_space -= 1

                # append solution
                solution.append("".join(current_words))

                # reset the running line 
                current_words = []
                current_line_length = 0
            
            # current word can be added to the running line
            current_words.append(words[i])
            current_line_length += len(words[i])

        # Append the last line 
        last_line = " ".join(current_words)
        last_line += " "*(maxWidth - len(last_line))

        solution.append(last_line)
        return solution
        