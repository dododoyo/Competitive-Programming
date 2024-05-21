n, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
# math
left, right = 0, n-1
while left < right:
  x = (numbers[right]-numbers[left])*100/(200-k)
  numbers[left] += x*(1-k/100)
  numbers[right] -= x
  left += 1
  right -= 1
print(min(numbers))
