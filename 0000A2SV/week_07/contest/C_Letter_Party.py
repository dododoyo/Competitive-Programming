def get_max(n,k,string,word):
  left = 0
  for right in range(len(string)):
    k -= string[right] != word
    if k < 0:
      k += string[left] != word
      left += 1
  return right - left + 1


n,k = map(int,input().split())
string = input()
solution = max(get_max(n,k,string,"a"),get_max(n,k,string,"b"))
print(solution)