from collections import defaultdict
n = int(input())
name_set,name_dict = set(),defaultdict(int)
for _ in range(n):
  name = input()
  if name in name_set:
    same_names = name_dict[name]
    new_name = name+str(same_names)
    print(new_name)
  else:
    name_set.add(name)
    print("OK")
  name_dict[name] += 1
  
