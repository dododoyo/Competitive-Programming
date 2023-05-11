n = int(input())
zerosOf1 = zerosOf2 = onesOf2 = onesOf1 = 0
for i in range(n):
    lnr = input()
    if lnr[0] == '0':zerosOf1 += 1
    else:onesOf1 += 1
    if lnr[2] == '0':zerosOf2 += 1
    else:onesOf2 += 1
print(min(zerosOf1,onesOf1)+min(onesOf2,zerosOf2))

