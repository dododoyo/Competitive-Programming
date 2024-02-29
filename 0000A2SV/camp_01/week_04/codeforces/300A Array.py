n = int(input())
nums = list(map(int, input().split()))
negatives, zeros, positives = [], [], []
for number in nums:
    if number == 0:zeros.append(0)
    elif number > 0:positives.append(number)
    else:negatives.append(number)
# length of negative numbers must always be odd
if len(negatives) % 2 == 0:
    zeros.append(negatives.pop())
if not positives:
    # if there are no positives
    # positives will be two negatives
    positives = negatives[:2]
    # and negatives have to be updated
    negatives = negatives[2:]
print(len(negatives), *negatives)
print(len(positives), *positives)
print(len(zeros), *zeros)
