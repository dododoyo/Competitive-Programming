s = input()
solution,i = [],0
if len(s) == 1:
    print('0')
    i+=1
while (i < len(s)):
    if s[i] == '.':
        solution.append('0');i+=1;
    elif s[i] == '-' and s[i+1] == '.':
        solution.append('1');i+=2;
    else:
        solution.append('2');i+=2;
print("".join(solution))