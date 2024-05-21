from collections import defaultdict
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
  current_row = list(input())
  dp = defaultdict(lambda: -1)

  def find_solution(i, j):
      if i == j:
          return i
      elif (i, j) in [("R", "B"), ("B", "R")]:
          return "G"
      elif (i, j) in [("R", "G"), ("G", "R")]:
          return "B"
      elif (i, j) in [("G", "B"), ("B", "G")]:
          return "R"


  def solve(p1, p2):
    if p2-p1 == 1:
      dp[p1, p2] = find_solution(
          current_row[p1], current_row[p2]) if dp[p1, p2] == -1 else dp[p1, p2]
      return dp[p1, p2]

    first_part = solve(p1, p2-1) if dp[p1, p2-1] == -1 else dp[p1, p2-1]
    second_part = solve(p1+1, p2) if dp[p1+1, p2] == -1 else dp[p1+1, p2]

    dp[p1, p2] = find_solution(first_part, second_part)

    return dp[p1, p2]

  print(solve(0, len(current_row)-1))
  # time = (n(n-1))/2

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()