#basically the question says you initially have an empty string
#and the task is to find out if you can change the empty string into
#the one given in the input only using the provided operation
#i.e putting a good string inside it at any position
t = int(input())  
for i in range(t):
    s = input()
    a,b,sol = 0,0,'YES'
    for x in s:
        if x == 'A':a+=1
        if x == 'B':b+=1
        #for any length starting from beginning there 
        # cannot be more B's than A's 
        if a < b:
            sol = 'NO';break
    #print algorithm's answer if the last character is B
    #any input with endind 'A' is invalid
    print(sol) if s[-1] == 'B' else print('NO')
