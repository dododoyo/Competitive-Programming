def min_change(s, n, k):
    possible_patterns = ['RGB' * (k // 3 + 1), 'GBR' * (k // 3 + 1), 'BRG' * (k // 3 + 1)]
    min_difference = float('inf')
    for i in range(n - k + 1):
        for pattern in possible_patterns:
            difference = 0 
            for j in range(k):
              difference += s[i+j] != pattern[j]
            min_difference = min(min_difference, difference)

    return min_difference

for _ in range(int(input())):
  n,k = map(int,input().split())
  s = input()
  '''
  find minimum number of
  change in the initial string 's'
  so that after the changes there will be substring of length k
  in 's' substring the infinite string "RGBRGBRGB ...".'''

  print(min_change(s,n,k))