from collections import defaultdict
import sys
import threading


def input(): return sys.stdin.readline().strip()


def main():
    # taking inputs
    days = int(input())
    days_score = []

    for i in range(days):
        points = [int(num) for num in input().split()]
        days_score.append(points)
    # end of taking inputs

    # memo = [[-1 for _ in range(4)]for _ in range(days)]
    # def find_max(current_day, prev_selection):
    #     # print(memo[current_day][prev_selection])
    #     if memo[current_day][prev_selection] != -1:
    #         return memo[current_day][prev_selection]

    #     solution = -float('inf')
    #     if current_day == 0:
    #         for i in range(3):
    #             if i != prev_selection:
    #                 solution = max(solution, days_score[current_day][i])

    #         memo[current_day][prev_selection] = solution
    #         return memo[current_day][prev_selection]

    #     for i in range(3):
    #         if i != prev_selection:
    #             current_score = days_score[current_day][i]
    #             prev_score = find_max(current_day-1, i)

    #             solution = max(solution, current_score+prev_score)

    #     memo[current_day][prev_selection] = solution

    #     return memo[current_day][prev_selection]
    
    # memo = [[-1 for _ in range(4)]for _ in range(days)]
    # for i in range(4):
    #     solution = -float('inf')
    #     for j in range(3):
    #             if i != j:
    #                 solution = max(solution, days_score[0][j])
    #     memo[0][i]= solution

    # for current_day in range(1,days):
    #     for prev_task in range(4):

    #         current_solution = 0 

    #         for current_task in range(3):
    #             if prev_task != current_task:

    #                 prev_solution = memo[current_day-1][current_task]
    #                 current_point = days_score[current_day][current_task]

    #                 current_solution = max(current_solution,prev_solution+current_point)
                
    #         memo[current_day][prev_task] = current_solution

    # # for the algorithm for to  find for all
    # # make it start from numbers different from 0,1,2
    # # select_none_of_given = find_max(days-1, 3)
    # # print(memo[days-1])

    # print(memo[days-1][3])
    prev_day = [-1 for _ in range(4)]

    for i in range(4):
        solution = -float('inf')
        for j in range(3):
                if i != j:
                    solution = max(solution, days_score[0][j])
        prev_day[i]= solution

    today = prev_day[:]

    for current_day in range(1,days):
        for prev_task in range(4):

            current_solution = 0 

            for current_task in range(3):
                if prev_task != current_task:

                    prev_solution = prev_day[current_task]
                    current_point = days_score[current_day][current_task]

                    current_solution = max(current_solution,prev_solution+current_point)
                
            today[prev_task] = current_solution
        prev_day = today[:]

    # for the algorithm for to  find for all
    # make it start from numbers different from 0,1,2
    # select_none_of_given = find_max(days-1, 3)
    # print(memo[days-1])
    print(prev_day[3])


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
