def get_max_index(arr):
  max_index = 0
  for i in range(len(arr)):
    if arr[i] > arr[max_index]:
      max_index = i 
  return max_index

def get_max_friends(a,b,c):
  a, b, c = a.copy(), b.copy(), c.copy() 
  max_index_a = get_max_index(a)
  b[max_index_a] = -1
  max_index_b = get_max_index(b)
  c[max_index_a],c[max_index_b] = -1,-1
  max_index_c = get_max_index(c)
  return a[max_index_a] + b[max_index_b]+c[max_index_c]

def solve():
  for _ in range(int(input())):
    n = int(input())
    a_ = list(map(int,input().split()))
    b_ = list(map(int,input().split()))
    c_ = list(map(int,input().split()))
    first_max = get_max_friends(a_,b_,c_)
    second_max = get_max_friends(a_,c_,b_)
    third_max = get_max_friends(b_,a_,c_)
    fourth_max = get_max_friends(b_,c_,a_)
    fifth_max = get_max_friends(c_,b_,a_)
    sixth_max = get_max_friends(c_,a_,b_)
    solution = max(first_max,second_max,third_max,fourth_max,fifth_max,sixth_max)
    print(solution)
solve()
"""
The issue implementation  without copying is that modifying the original lists `a`, `b`, and `c` in the `get_max_friends` function. This means that after the first call to `get_max_friends`, the lists `a`, `b`, and `c` have been changed, and the subsequent calls to `get_max_friends` are not working with the original lists.

To fix this, you create copies of the lists in the `get_max_friends` function.
```
Now, each call to `get_max_friends` will work with a fresh copy of the lists, and the order of the calls won't matter."""