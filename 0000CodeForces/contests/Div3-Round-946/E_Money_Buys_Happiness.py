import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()
'''
def main():
  for _ in range(int(input())):
    months, salary = map(int, input().split())
    happiness_cost = [[0, 0] for _ in range(months)]

    for current_month in range(months):
      cost, happiness = map(int, input().split())
      happiness_cost[current_month] = [cost, happiness]

    def find_happ(index, current_saving):
      if index == months-1:
        if happiness_cost[index][0] <= current_saving:
          return happiness_cost[index][1]
        else:
          return 0

      not_take = find_happ(index+1, current_saving+salary)
      take = 0

      if happiness_cost[index][0] <= current_saving:
          current_saving -= happiness_cost[index][0]
          take = happiness_cost[index][1] +  find_happ(index+1, current_saving+salary)

      return max(take, not_take)

    print(find_happ(0, 0))
'''

def main():
  for _ in range(int(input())):
    months, salary = map(int, input().split())
    happiness_cost = [[0, 0] for _ in range(months)]
    for current_month in range(months):
      cost, happiness = map(int, input().split())
      happiness_cost[current_month] = [cost, happiness]

    dp = [[0 for _ in range(salary * months + 1)] for _ in range(months+1)]

    for i in range(salary*months + 1):
          # if index == months-1:
        if happiness_cost[months-1][0] <= i:
          dp[months-1][i] = happiness_cost[months-1][1]
        else:
          dp[months-1][i] = 0

    for i in range(months-2, -1, -1):
      for j in range(salary * months + 1):
        not_take = dp[i+1][j] if j + salary < salary * months + 1 else 0
        take = 0
        if happiness_cost[i][0] <= j:
          take = happiness_cost[i][1] + (dp[i+1][j-happiness_cost[i][0]+salary] if j - happiness_cost[i][0] + salary < salary * months + 1 else 0)
        dp[i][j] = max(take, not_take)

    print(dp[0][0])

if __name__ == '__main__':
  main()
if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()