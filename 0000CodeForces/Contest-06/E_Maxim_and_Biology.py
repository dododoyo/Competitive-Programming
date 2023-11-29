n = int(input())
s = input()
minOp = float('inf')

for i in range(n - 3):
    #caculate the cost of converting each substring to it's respective genome equivalent
    #and get the minimum for each
    choice = abs(ord('A') - ord(s[i]))
    OpA = min(choice, 26 - choice)
    choice = abs(ord('C') - ord(s[i + 1]))
    OpC = min(choice, 26 - choice)
    choice = abs(ord('T') - ord(s[i + 2]))
    OpT = min(choice,26 - choice)
    choice = abs(ord('G') - ord(s[i + 3]))
    OpG = min(choice,26 - choice)
    #find the minimum for all windows
    minOp = min(minOp,OpA + OpC + OpT + OpG)

print(minOp)
