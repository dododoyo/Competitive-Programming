def findPoints(arr):
  totalPoints = 0;
  for i in range(10):
    for j in range(10):
      if arr[i][j] == "X":
        if 3 < i < 6 and 3 < j < 6:
          totalPoints += 5;
        elif 2 < i < 7 and 2 < j < 7:
          totalPoints += 4;
        elif 1 < i < 8 and 1 < j < 8:
          totalPoints += 3;
        elif 0 < i < 9 and 0 < j < 9:
          totalPoints += 2;
        else:
          totalPoints += 1;


  return totalPoints


t = int(input())

for _ in range(t):
  arrowsFired = [0]*10
  # print(arrowsFired);
  for i in range(10):
    row = list(input())
    arrowsFired[i] = row;
  print(findPoints(arrowsFired));

