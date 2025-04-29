for i in range([int(i) for i in input().split()][0]):
	n = [int(i) for i in input().split()][0]
	arr = [int(i) for i in input().split()]
	arr = {index:num for num,index in enumerate(arr)}
	
	solution = ["0"]*len(arr)
	
	minn = 10**10
	maxx = -1
	
	for i in range(1, len(arr)+1):
		minn = min(minn, arr[i])
		maxx = max(maxx, arr[i])
		
		if maxx - minn == i-1:
			solution[i-1] = "1"
			
	print(''.join(solution))