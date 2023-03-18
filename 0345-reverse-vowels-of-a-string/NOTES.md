### we will have 4 possiblities
#1 --> character at both pointers is consonants
# do nothing
#2 --> character at left pointers is vowel
# character at right pointer is consonant
# decrease right pointer to look for vowels
#3 --> character at right pointers is vowel
# character at left pointer is consonant
# increase left pointer to look for vowels
#4 --> if both are vowels the swap them