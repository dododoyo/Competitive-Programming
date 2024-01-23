inputs =  list(map(int,input().split()))
'''the number of drinks that can be provided 
   are determined by three factors 1limes 2salt 3drinks'''
# variable abbrivation 
# n_l needed lime || a_d available drink 
n_l = inputs[0]
a_d = inputs[1]*inputs[2]
a_l = inputs[3]*inputs[4]
a_s = inputs[5]
'''total number of times people who can 
drink softdrink alone'''
d = (a_d//inputs[6])//inputs[0]
'''total number oftimes people
who eat salt alone'''
s =  (a_s//inputs[7])//inputs[0]
'''total number of times 
people eat limes alone'''
l = a_l//inputs[0]
if d<=s and d<=l:
    print(d)
elif s<=d and s<=l:
    print(s)
else:
    print(l)