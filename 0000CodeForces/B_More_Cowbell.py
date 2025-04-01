from sys import stdin
def input(): return stdin.readline().strip()

cowbells,boxes = [int(i) for i in input().split()]
cowbell_size = [int(i) for i in input().split()]

# find minimum boxes size that will contain 
# all the cowbells if we have k of it 

def canFit(box_size):
  min_cowbell_index, max_cowbell_index = 0, cowbells - 1 
  used_boxes = 0

  while min_cowbell_index <= max_cowbell_index:
      if min_cowbell_index != max_cowbell_index and cowbell_size[min_cowbell_index] + cowbell_size[max_cowbell_index] <= box_size:
          min_cowbell_index += 1 
      
      # take max regardless
      max_cowbell_index -= 1  
      used_boxes += 1

  return used_boxes <= boxes

left,right = max(cowbell_size),sum(cowbell_size)
solution = right

while left <= right:
  middle = left + (right-left)//2

  if canFit(middle):
    solution = middle
    right = middle - 1
  else:
    left = middle + 1

print(solution)