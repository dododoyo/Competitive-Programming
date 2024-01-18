status = input()
'''
 the opportunity to delete the 
 last digit or the digit before 
 last from the state of his bank 
 account no more than once.
'''

if status[0] == "-":
  # the number is negative
  last_removed = status[:-1] 
  second_last_removed = status[:-2] + status[-1]
  solution = max(int(last_removed),int(second_last_removed))
  # maximum of the negative 
  # have the less 
else:
  solution = status

print(solution)