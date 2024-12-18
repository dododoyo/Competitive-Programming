# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        # use two stacks one for frequency of current word 
        # the other to register the current word 
        
        number_stack,string_stack = [],[]
        curr_index, n = 0 , len(s)

        while curr_index < n:
            # current char is number 
            if s[curr_index].isdigit():
                num = ""
                while curr_index < n and s[curr_index].isdigit():
                    num += s[curr_index]
                    curr_index += 1
                # add it to the num stack 
                number_stack.append(int(num))
            else:
            # current char is '[', ']', or 'isalpha'
                # char is ']'
                if s[curr_index] == ']':
                    # we need to process the two stacks
                    word = ''
                    while string_stack and string_stack[-1] != "[":
                        word = string_stack.pop() + word
                    freq = number_stack.pop()

                    # remove "[" because it is used as a marker 
                    # to show the end of current string
                    string_stack.pop()

                    # decode -> multiplying char by freq-times from stack
                    decoded = word*freq

                    # and append the result to solution
                    string_stack.append(decoded)

                # char isalpha or '['
                else:  
                    # append it to string stack 
                    string_stack.append(s[curr_index])
                curr_index += 1

        return "".join(string_stack)
