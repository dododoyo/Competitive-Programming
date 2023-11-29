def k_string(k,s):
    char_freq = [0]*26
    for i in s:char_freq[ord(i)-97]+=1;
    solution,i = [""]*len(s),0
    for l in range(len(char_freq)):
            if char_freq[l]%k != 0:return -1
            else:
                freq = char_freq[l]//k
                while freq != 0:
                     solution[i]=chr(l+97);i+=1;freq-=1

    return ("".join(solution))*k

k = int(input())
s = input()
print(k_string(k,s))
