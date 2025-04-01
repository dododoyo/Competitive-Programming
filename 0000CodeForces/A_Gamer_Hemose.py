from sys import stdin
def input(): return stdin.readline().strip()


for _ in range([int(i) for i in input().split()][0]):
  weapons,enemy = [int(i) for i in input().split()]
  weapon_damage = sorted([int(i) for i in input().split()])
  max1,max2 = weapon_damage[-1],weapon_damage[-2]

  def canKill(x):
    killingPower = (max1+max2)*(x//2) + max1*(x%2)

    return enemy <= killingPower


  solution = enemy
  left,right = 1,enemy 

  while left <= right:
    middle = left + (right-left)//2

    if canKill(middle):
      solution = middle
      right = middle - 1
    else:
      left = middle + 1

  print(solution)