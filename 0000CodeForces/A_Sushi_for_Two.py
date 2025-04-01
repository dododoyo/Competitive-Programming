n = [int(i) for i in input().split()][0]
sushi = [int(i) for i in input().split()]


def valid(x):
    n = len(sushi)
    index = 0
    while index < n:
        count = 1
        
        while index + 1 < n and sushi[index+1] == sushi[index]:
            count += 1
            index += 1

        if count >= x:
            valid_finder = index + 1

            if valid_finder < n:
                opp_val = 2 if sushi[index] == 1 else 1
                opp_count = 0

                while valid_finder < n and sushi[valid_finder] == opp_val:
                    opp_count += 1
                    valid_finder += 1
                    
                if opp_count >= x:
                    return True
                
        index += 1
    return False

  # validate the next x consequative 
    # if true return True
    # else start from the broken

left,right = 1,n
solution = 1

while left <= right:
  middle = left + (right-left)//2
  # print(middle,valid(middle))

  if valid(middle):
    solution = middle
    left = middle + 1
  else:
    right = middle - 1

print(solution*2)