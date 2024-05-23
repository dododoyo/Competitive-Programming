# from collections import defaultdict

n = int(input())
probabilities = [float(num) for num in input().split()]

memo = [[0 for _ in range(n+1)] for _ in range(n+1)]


# def find_prob(index,head_count):
#   if index == -1:
#     tail_count= n - head_count
#     return int(head_count > tail_count)

#   if memo[index][head_count] != -1:
#     return memo[index][head_count]

#   if_head = probabilities[index]*find_prob(index-1,head_count+1)
#   if_tail = (1-probabilities[index])*find_prob(index-1,head_count)

#   memo[index][head_count] = if_head + if_tail

#   return memo[index][head_count]

# print(find_prob(n-1,0))


# probability of getting zero heads from zero coins is one
memo[0][0] = 1

for index in range(1, n+1):
    for head_count in range(index+1):
        if_head, if_tail = 0, 0

        if head_count != 0:
            if_head = probabilities[index-1] * memo[index-1][head_count-1]

        if_tail = (1 - probabilities[index-1]) * memo[index-1][head_count]

        memo[index][head_count] = if_tail + if_head

solution = sum(memo[n][head_count] for head_count in range((n+1)//2, n+1))
print(solution)
