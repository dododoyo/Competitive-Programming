# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        number_stack,string_stack = [],[]
        curr_index = 0
        while curr_index < len(s):
            if s[curr_index].isdigit():
                digit = ""
                while s[curr_index].isdigit():
                    digit += s[curr_index]
                    curr_index += 1
                number_stack.append(int(digit))
            else:
                if s[curr_index] == "]":
                    curr_str = ""
                    while string_stack and string_stack[-1] != "[":
                        curr_str = string_stack.pop() + curr_str
                    string_stack.pop()
                    string_stack.append(number_stack.pop()*curr_str)
                    print(curr_str)
                else:
                    string_stack.append(s[curr_index])
                curr_index += 1
        return "".join(string_stack)