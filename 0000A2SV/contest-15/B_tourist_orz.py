for _ in range(int(input())):
  n, z = map(int, input().split())
  integers = [int(num) for num in input().split()]
  solution = 0
  # no need to do z$number
  for number in integers:
    solution = max(solution, z | number)
  print(solution)
