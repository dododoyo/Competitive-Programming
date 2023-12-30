t = int(input())
solutions = []
for j in range(t):
  input()
  not_found = 1
  for i in range(8):
    line = input()
    var = line.find("#.#")
    if var != -1 and not_found:
      solutions.append([i+2,var+2])
      not_found = 0
for solution in solutions:
  print(solution[0],solution[1])