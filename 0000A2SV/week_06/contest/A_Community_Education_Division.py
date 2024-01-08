for _ in range(int(input())):
  rating = int(input())
  if rating <= 1399:
    print("Division 4")
  elif rating >= 1400 and rating <= 1599:
    print("Division 3")
  elif rating >= 1600 and rating <= 1899:
    print("Division 2")
  else:
    print("Division 1")
