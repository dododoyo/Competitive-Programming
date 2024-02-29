n, m = map(int, input().split())
correct = list(map(int, input().split()))
wrong = list(map(int, input().split()))
correct_min = correct_max = correct[0]
min_bound = min(wrong)
for second in correct:
    if second > correct_max:correct_max = second
    if second < correct_min:correct_min = second
solution = max(2*correct_min,correct_max)
if  solution < min_bound:
    print(solution)
else:
    print(-1)
