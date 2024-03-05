n = int(input())
upper_sum = lower_sum = 0
has_odd_even_domino = False
# even,odd and odd,even result in -1

for _ in range(n):
    x, y = map(int, input().split())
    upper_sum += x
    lower_sum += y
    if (x % 2 != y % 2):
        has_odd_even_domino = True

if upper_sum % 2 == 0 and lower_sum % 2 == 0:
    print(0)
elif has_odd_even_domino and upper_sum % 2 != 0 and lower_sum % 2 != 0:
    print(1)
else:
    print(-1)