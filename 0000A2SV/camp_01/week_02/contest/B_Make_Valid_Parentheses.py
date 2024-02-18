def solver(brackets):
  max_len = 0
  stack = []

  # regular parentheses == every open bracket is closed
  # return the length of the longest regular parentheses

  for bracket in brackets:
    if bracket == "(":
      stack.append("(") 
    else:
      if stack and stack[-1] == "(":
        stack.pop()
        max_len += 2
  return max_len

print(solver(input()))
