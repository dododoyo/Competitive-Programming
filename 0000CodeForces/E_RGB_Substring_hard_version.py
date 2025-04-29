for _ in range(int(input())):
  n, k = map(int, input().split())
  s = input()

  def foo(t):
    ans = len(s)
    window = 0
    for i in range(k - 1):
      if s[i] != t[i]:
        window += 1
      
    for i in range(k - 1, n):
      if s[i] != t[i]:
        window += 1
      
      ans = min(ans, window)

      if s[i - k + 1] != t[i - k + 1]:
        window -= 1

    
    return ans
  
  s1 = 'RGB' * (n // 3) + ('R' if n% 3 == 1 else '') + ('RG' if n % 3 == 2 else '')
  s2 = 'GBR' * (n // 3) + ('G' if n% 3 == 1 else '') + ('GB' if n % 3 == 2 else '')
  s3 = 'BRG' * (n // 3) + ('B' if n% 3 == 1 else '') + ('BR' if n % 3 == 2 else '')
  print(min(
    foo(s1),
    foo(s2),
    foo(s3)
  ))