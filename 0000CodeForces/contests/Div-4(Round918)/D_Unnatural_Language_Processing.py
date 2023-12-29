def solve(n,s):
  """
  for each of the words it must start with a consonant and then the second element is vowel even if it is three word or two words long . . .

  Doing this will guarantee us we get
  a dot before each word and then remove the first dot when returning
  """
  for c in "dcb":
      for v in "ea":
          s = s.replace(c + v, "." + c + v)
  return s[1:]

for _ in range(int(input())):
  n = int(input())
  s = input()
  print(solve(n,s))
