solution = 0
for _ in range(int(input())):
  current_question_vote = list(map(int,input().split()))
  solution += sum(current_question_vote) > 1;
print(solution)