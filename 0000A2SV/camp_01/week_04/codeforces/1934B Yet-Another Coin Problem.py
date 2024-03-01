for t in range(int(input())):
	n = int(input())
	ones = n % 3 
	threes,tens = (n - ones) // 3 , 0
	# get to total sum into threes and ones
	while ones > 0 and threes >= 3:
		# convert (3 threes) and (1 one) to 1 ten
		threes, ones, tens = threes - 3, ones - 1, tens +1
		
  # how many fifteens can be made from the given threes
	fifteens = threes // 5
	# update remaining threes
	threes = threes % 5
	
  # how many sixes can be made from the given threes
	six = threes // 2
  # update threes
	threes = threes % 2

	print(ones+ threes+six+ tens+fifteens)