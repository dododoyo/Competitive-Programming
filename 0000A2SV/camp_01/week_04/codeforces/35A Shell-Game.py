with open('input.txt', 'r') as f:
    lines = f.readlines()

correct_index = int(lines[0])
for line in lines[1:]:
    cup_1, cup_2 = map(int, line.split())
    if cup_1 == correct_index:
        correct_index = cup_2
    elif cup_2 == correct_index:
        correct_index = cup_1

with open('output.txt', 'w') as f:
    f.write(str(correct_index))
