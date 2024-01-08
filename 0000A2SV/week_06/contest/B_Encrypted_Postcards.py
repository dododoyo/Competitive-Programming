for _ in range(int(input())):
  n = int(input())
  word,solution = input(),[]
  holder,seeker = 0,1
  while seeker < n and holder < n:
    if word[seeker] == word[holder]:
      solution.append(word[holder])
      seeker += 1
      holder = seeker
    seeker += 1
  print("".join(solution))
