# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

'''find the smallest and the largest of the 
numbers that have length m and sum of digits s.
'''
m, s = map(int, input().split())

if m == 1 and s == 0:
    print(0, 0)
elif s > 9 * m or s == 0:
    print(-1, -1)
else:
    smallest = 10**(m-1) + sum(10**(i//9) for i in range(s-1))
    largest = sum(10**(m-1-i//9) for i in range(s))
    print(smallest, largest)