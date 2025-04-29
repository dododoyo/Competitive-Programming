#########################################################################
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from math import ceil, sqrt, gcd
import heapq

def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return [list(map(int, inp().split())) for _ in range(rows)]

# setrecursionlimit(10**6)
#########################################################################

#  The core idea is to analyze the maximum distance a clock 
# can be from either end of the line and relate that to its initial time.


"""
The code checks if it's possible to survive indefinitely by strategically moving between clocks and resetting them. The core idea is to analyze the maximum distance a clock can be from either end of the line and relate that to its initial time.

Here's a breakdown of the logic:

The Problem's Core Constraint: The fundamental constraint is that a clock's value must always be greater than 0. If a clock's value reaches 0, you lose. The crucial part is understanding how quickly a clock's value decreases and how long it takes to "rescue" it by reaching and resetting it.

Worst-Case Scenario: Consider the worst-case scenario for a particular clock. Let's say you are currently not at that clock. The furthest you could be from a clock i is when you're at one of the ends of the line. The maximum distance you might need to travel to reach clock i is max(i, n - (i + 1)). i is the distance from the left end (starting from 0), and n - (i + 1) is the distance from the right end. We take the maximum of these two distances to account for the worst-case.

Round Trip: If you are at the farthest end of the array, the maximum distance we calculated in point 2 means that the clock must support 2x more steps to get to the clock and back to the previous position.

Survival Condition: For you to be able to "save" clock i, its initial value (arr[i]) must be large enough to withstand the time it takes for you to travel the maximum distance and return. Specifically, arr[i] must be greater than twice the maximum distance. We multiply the maximum distance by 2 because it represents a round trip: you go to the clock and then potentially return to your previous location (or another clock). This ensures that the time will never reduce to 0 when resetting that clock.

Iteration and Check: The code iterates through each clock (for i in range(n)) and checks this survival condition: if arr[i] <= 2 * (max(i, n - (i + 1))). If, for any clock, this condition is true, it means that clock cannot be saved in the worst-case scenario, and you will eventually lose. Therefore, the code prints "NO".

"YES" Condition: If the loop completes without finding any clock that violates the survival condition (the else block associated with the for loop), it means all clocks can be saved indefinitely, and the code prints "YES".

In Simple Terms:

The code is essentially saying, "For each clock, imagine you're as far away from it as possible. Does that clock have enough initial time to survive until you can get back to it and return from the other end? If even one clock doesn't have enough time, you'll eventually lose. If all clocks have enough time, you can keep going forever."
"""

for _ in range(int(input())):
	n = ls()[0]
	arr = ls()
	
	for i in range(n):
		if arr[i] <= 2*(max(i,n-(i+1))):
			print('NO')
			break
	else:
		print('YES')