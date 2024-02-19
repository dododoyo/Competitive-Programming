t = int(input())
numbers = [0]*(200009)
numbers[1] = 1
for i in range(2, 200009):
	numbers[i] = numbers[i-1] + sum(map(int, list(str(i))))

for i in range(t):
	n = int(input())
	print(numbers[n])