def is_same_race(dwarf1,dwarf2):
  n,m,difference = len(dwarf1),len(dwarf2),[]
  if n != m:return "NO"
  for i in range(n):
    if dwarf1[i] != dwarf2[i] and len:
      if len(difference) == 1:
        if dwarf1[difference[0]] != dwarf2[i]  or  dwarf1[i] != dwarf2[difference[0]]:
          return "NO"
      difference.append(i)
  return "YES" if len(difference) == 2 else "NO"

print(is_same_race(input(),input()))