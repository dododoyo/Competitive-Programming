# if w underline it 
# if vv underline one of the v

# find subarrays with v repeated 
# find the number of w
for _ in range(int(input())):
  s = input()
  underlines = 0 
  left,right = 0,0
  while right < len(s):
    if s[right] == "w":
      underlines += 1
      right = right+1
      left = right
    else:
      while right < len(s) and s[right] == "v":
        right += 1
      else:
        underlines += (right-left-1)
        left = right
  print(underlines)
