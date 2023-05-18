guests = list(input())
hosts = list(input())
shuffled = list(input())
freq_each = [0]*26
'''since our string consists of only 
upper case english characters we can use 
and array of size 26 to register the frequency 
of each character in the first two strings and 
decrease it's frequency with the last string 
if the frequency of a character is zero it means
the character exists both in the strings 
if not it doesn't and if  all the frequency of characters
is zero this means all the characters exist in both strings'''
for i in guests:
    freq_each[ord(i)-65] += 1
for i in hosts:
    freq_each[ord(i)-65] += 1
for i in shuffled:
    freq_each[ord(i)-65] -= 1
counter = 0
for i in freq_each:
    if i == 0:counter+=1
print('YES') if counter == 26 else print('NO')
