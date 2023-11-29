"""
used stack and pointers
"""

s = input()
hello_stack = ["h","e","l","l","o"]
finder_index,s_index,  = 4,len(s)-1

while s_index > -1:
  if hello_stack and hello_stack[-1] == s[s_index]:
    hello_stack.pop()
  # print(hello_stack,s_index)
  s_index -= 1


print("YES") if not hello_stack else print("NO")
