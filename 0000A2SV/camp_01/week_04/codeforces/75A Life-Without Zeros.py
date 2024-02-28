a = input()
b = input()

original_a = a
original_b = b
original_c = str(int(a)+int(b))

filtered_a = []
for i in a:
  if i != "0":
    filtered_a.append(i)

filtered_b = []
for i in b:
  if i != "0":
    filtered_b.append(i)

filtered_c = []
for i in original_c:
  if i != "0":
    filtered_c.append(i)

new_a = "".join(filtered_a)
new_b = "".join(filtered_b)
new_c = "".join(filtered_c)

if int(new_a) + int(new_b) == int(new_c):
  print("YES")
else:
  print("NO")