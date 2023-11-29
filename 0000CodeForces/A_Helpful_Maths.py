#solution without custom functions
def countsorter(arr):
    ones,twos,threes = 0,0,0
    for i in arr:
        if i == '1':ones+=1
        elif i == '2':twos+=1
        else :threes+=1
    j = 0
    while (j < len(arr)):
        while ones > 0:arr[j] = '1';j+=1;ones-=1
        while twos > 0:arr[j] = '2';j+=1;twos-=1
        while threes > 0:arr[j] = '3';j+=1;threes-=1
    #print(arr)
    return arr
def spliter(the_string):
    each_elmnt = []
    str_so_far = ""
    for i in the_string:
        if i == '+':
            each_elmnt.append(str_so_far)
            str_so_far = ''
        else:
            str_so_far += i
    if str_so_far != '':
        each_elmnt.append(str_so_far)
    return each_elmnt
def joiner(arr):
    solution = arr[0]
    for i in range(1,len(arr)):
        solution += '+' + arr[i]
        #print(solution)
    return solution

print(joiner(countsorter(spliter(input()))))
    
