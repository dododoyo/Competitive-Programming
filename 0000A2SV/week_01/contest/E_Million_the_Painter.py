n = int(input())
s = input()

solution = 'No'

if s[0] == '?' or s[-1] == '?':
	solution =	'Yes'
for i in range(1, n-1):
	if s[i] == '?' and not (s[i-1] != s[i+1] and s[i-1] != '?' and s[i+1] != '?'):
		solution = 'Yes'
	if s[i] != '?' and s[i] == s[i-1]:
		solution = 'No'
		break

if n > 1 and s[-1] != '?' and s[-1] == s[-2]:
	solution = 'No'

print(solution)

