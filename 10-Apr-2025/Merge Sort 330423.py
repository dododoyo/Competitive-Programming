# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

from sys import stdin
def input(): return stdin.readline().strip()


n,k = [int(i) for i in input().split()]
if k % 2 == 0:
    print(-1)
else:
  # initial call for the first call
  k -= 1
  a = [i+1 for i in range(n)]

  # right is exclusive
  def reverseMergeSort(l,r):
      global k

      # only one element left 
      if r-l < 2:
        return
      
      # you can't make moves
      if k == 0:
        return 
      
      k -= 2
      m = (l+r)//2
      a[m], a[m-1] = a[m-1], a[m]

      reverseMergeSort(l,m)
      reverseMergeSort(m, r)

  reverseMergeSort(0, n)

  if k != 0:
    print(-1)
  else:
    print(' '.join([str(i) for i in a]))