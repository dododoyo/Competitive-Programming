"""
used pointers
"""
s = input()
finder_index,s_index,  = 4,len(s)-1

while s_index > -1:
  if finder_index > -1 and "hello"[finder_index] == s[s_index]:finder_index -= 1
  s_index -= 1

print("NO") if finder_index != -1 else print("YES")
