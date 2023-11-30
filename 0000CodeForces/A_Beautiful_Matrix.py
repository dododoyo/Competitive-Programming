location=[]
for i in range(5):
  row = list(input().split())
  # print(row)
  if "1" in row:
    location.append(i+1)
    for index,val in enumerate(list(row)):
      # print(row[index])
      if val == "1":
        location.append(index+1)

  # print(abs(location[0]-2)+abs(location[1]-2))
  print(location)
      










































# solution = [0,0]
# for i in range(5):
#     row = input()
#     for j in range(0,9,2):
#         if row[j] == '1':
#             solution = [i+1,int(j/2)+1]
# swaps = abs(solution[0] - 3)
# swaps += abs(solution[1] - 3)
# print(swaps)
