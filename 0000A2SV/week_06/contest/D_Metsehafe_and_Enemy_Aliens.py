for _ in range(int(input())):
  n = int(input())
  hordes = [int(i) for i in input().split()]
  hordes.sort()
  left,right = 0,n-1
  current_attacks,total_attacks = 0,0
  while left < right:
    if current_attacks < hordes[right]:
      total_attacks += hordes[left]
      current_attacks += hordes[left]
    else:
      total_attacks += 1
      current_attacks -= hordes[right]
      right -= 1
    left += 1
    # print(current_attacks,total_attacks)
  print(current_attacks,total_attacks)
  
  total_attacks += (current_attacks==total_attacks and current_attacks != 0)
  
  # print(total_attacks)
  # print()
