from sys import stdin
def input(): return stdin.readline().strip()

for _ in range([int(i) for i in input().split()][0]):
  programmers,mathematicians = sorted([int(i) for i in input().split()])
  moreMath = min(programmers,mathematicians//3)
  equalMath = min(programmers//2,mathematicians//2)

  leftProsEqual = programmers - equalMath*2
  leftMathsEqual = mathematicians - equalMath*2
  leftAdditionalEqual = min(min(leftProsEqual,leftMathsEqual),max(leftProsEqual,leftMathsEqual)//3)

  leftMathForMoreMaths = mathematicians - 3*moreMath
  leftProsForMoreMaths = programmers - moreMath

  equalAdditions = min(leftMathForMoreMaths//2,leftProsForMoreMaths//2)
  skewedAdditions = min(min(leftMathForMoreMaths,leftProsForMoreMaths),max(leftMathForMoreMaths,leftProsForMoreMaths)//3)

  leftMoreMath = max(equalAdditions,skewedAdditions)


  def isValid(teams):
    
    # can make three maths team
    if moreMath + leftMoreMath >= teams:
      return True 
    
    # 2 maths and 2 programmers
    if equalMath + leftAdditionalEqual >= teams:
      return True


    return False


  left,right = 0,min(programmers,mathematicians)
  solution = 0

  while left <= right:
    middle = left + (right-left)//2

    if isValid(middle):
      solution = middle 
      left = middle + 1
    else:
      right = middle - 1

  print(solution)



