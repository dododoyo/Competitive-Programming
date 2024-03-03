with open("input.txt", "r") as file:
    lines = file.readlines()

two_n, handedness = int(lines[0]), lines[1]
n = two_n//2

with open("output.txt", "w") as file:
    for i in range(n):
        cf_index = i+1
        if handedness[i] == 'R':
            file.write(f"{cf_index+n} {cf_index}\n")
        else:
            file.write(f"{cf_index} {cf_index+n}\n")

