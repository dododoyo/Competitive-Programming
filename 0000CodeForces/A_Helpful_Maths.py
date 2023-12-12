num_map = {"1":0,'2':1,'3':2}
nums = input().split("+")
counter = [0,0,0]
for number in nums:
  counter[num_map[number]] += 1

solution_index = 0
for _ in range(counter[0]):
  nums[solution_index] = "1"
  solution_index +=1 
for _ in range(counter[1]):
  nums[solution_index] = "2"
  solution_index +=1 
for _ in range(counter[2]):
  nums[solution_index] = "3"
  solution_index +=1 

print("+".join(nums));
