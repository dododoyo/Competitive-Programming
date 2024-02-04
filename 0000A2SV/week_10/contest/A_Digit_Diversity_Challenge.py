def is_unique(num):
    digits = [0]*10
    while num:
        current_digit = num%10
        if digits[current_digit] == 1:
            return False
        digits[current_digit] = 1
        num //= 10
    return True

l, r = map(int, input().split())
for i in range(l, r+1):
    if is_unique(i):
        print(i)
        break
else:
    print(-1)