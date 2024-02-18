n = int(input())
arr = list(map(int,input().split()))
negatives,positives = 0,0
total_negatives,total_positives = 0,0
for number in arr:
  prev_pos,prev_neg = positives,negatives
  if number > 0:
      positives += 1
  else:
      positives = prev_neg
      negatives = prev_pos+1
  total_negatives += negatives
  total_positives += positives

print(total_negatives,total_positives)