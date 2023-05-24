#What the question basically asks
#is to check whether the two strings 
# are reverses of each other
word1 = input()
word2 = input()
i = 0
while i < len(word1):
    if word1[i] == word2[len(word2)-i-1]:i+=1
    else:print('NO');exit();
print('YES')