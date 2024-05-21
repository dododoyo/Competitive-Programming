for _ in range(int(input())):
  word = input()
  n = len(word)

  if n%2:
    print("NO")
  else:
    print("YES" if word[:n//2] == word[n//2:] else "NO")