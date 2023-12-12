def keyboard_checker(s):
    each_freq = [0]*26
    for i in s:
        each_freq[ord(i)-97]+=1
    solution =[""]
    for i in range(26):
        if  each_freq[i]%2 != 0:solution.append(chr(i+97))
    return "".join(solution)
for i in range(int(input())):
    print(keyboard_checker(input()))
