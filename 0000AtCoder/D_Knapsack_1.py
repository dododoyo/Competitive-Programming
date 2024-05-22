import sys
import threading
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def main():
    # take inputs
    items, knapsack_capacity = map(int, input().split())
    weights, values = [0]*items, [0]*items
    for i in range(items):
        item_weight, item_value = map(int, input().split())
        weights[i] = item_weight
        values[i] = item_value
    # end of taking inputs

    last_index = [0]*(knapsack_capacity+1)

    for remaining_capacity in range(weights[0], knapsack_capacity+1):
        last_index[remaining_capacity] = values[0]

    current_index = last_index[:]

    for index in range(1, items):
        for remaining_capacity in range(knapsack_capacity+1):
            not_take = last_index[remaining_capacity]
            take = -float('inf')

            if remaining_capacity >= weights[index]:
                new_capacity = remaining_capacity-weights[index]
                take = values[index] + last_index[new_capacity]

            current_index[remaining_capacity] = max(take, not_take)
        last_index = current_index[:]

    print(last_index[knapsack_capacity])

    # memo = [[0 for _ in range(knapsack_capacity+1)]for _ in range(items)]

    # for remaining_capacity in range(weights[0],knapsack_capacity):
    #     memo[0][remaining_capacity] = values[0]

    # for index in range(1,items):
    #     for remaining_capacity in range(knapsack_capacity+1):

    #         not_take = memo[index-1][remaining_capacity]

    #         take = -float('inf')

    #         if remaining_capacity >= weights[index]:
    #             new_capacity = remaining_capacity-weights[index]

    #             take = values[index] + memo[index-1][new_capacity]

    #         memo[index][remaining_capacity] = max(take, not_take)

    # print(memo[items-1][knapsack_capacity])

    # dp = defaultdict(lambda: -1)
    # def find_max(index, remaining_capacity):
    #     if dp[index, remaining_capacity] != -1:
    #         return dp[index, remaining_capacity]

    #     if index == 0:
    #         if remaining_capacity >= weights[index]:
    #             dp[index, remaining_capacity] = values[index]
    #             return dp[index, remaining_capacity]
    #         else:
    #             dp[index, remaining_capacity] = 0
    #             return dp[index, remaining_capacity]

    #     not_take = find_max(index-1, remaining_capacity)
    #     take = -float('inf')

    #     if remaining_capacity >= weights[index]:
    #         take = values[index] + \
    #             find_max(index-1, remaining_capacity-weights[index])

    #     dp[index, remaining_capacity] = max(take, not_take)
    #     return dp[index, remaining_capacity]

    # print(find_max(items-1, knapsack_capacity))


if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
