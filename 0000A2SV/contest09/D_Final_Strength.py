from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    strengths = list(map(int, input().split()))
    n_s = len(strengths)
    strengths = [(i, strengths[i]) for i in range(n_s)]

    def merge(left_arr, right_arr):
        lp, rp = 0, 0
        ll, rl = len(left_arr), len(right_arr)
        left_incremented,right_incremented = [0]*ll,[0]*rl

        for i in range(ll):
            while rp < rl and left_arr[i][1] > right_arr[rp][1]:
                rp += 1
            left_incremented[i] = rp
        for i in range(rl):
            while lp < ll and right_arr[i][1] > left_arr[lp][1]:
                lp += 1
            right_incremented[i] = lp

        right_arr = [(right_arr[i][0],(right_arr[i][1]+right_incremented[i])) for i in range(rl)]
        left_arr = [(left_arr[i][0],(left_arr[i][1]+left_incremented[i])) for i in range(ll)]
        lp, rp, solution = 0, 0, []
        
        while lp < ll and rp < rl:
            if left_arr[lp][1] <= right_arr[rp][1]:
                solution.append(left_arr[lp])
                lp += 1
            else:
                solution.append(right_arr[rp])
                rp += 1
        solution.extend(left_arr[lp:])
        solution.extend(right_arr[rp:])

        return solution

    def mergeSort(low, high):
        if low == high:
            return [strengths[low]]
        middle = low + (high-low)//2
        left_arr = mergeSort(low, middle)
        right_arr = mergeSort(middle+1, high)
        return merge(left_arr, right_arr)
    
    solution = mergeSort(0, n_s-1)
    real_solution = [0]*n_s
    for i in range(n_s):
        real_solution[solution[i][0]] = solution[i][1]
    print(*real_solution)
