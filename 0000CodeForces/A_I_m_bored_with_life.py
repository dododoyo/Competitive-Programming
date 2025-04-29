import sys
from sys import stdin
sys.setrecursionlimit(1 << 25)
import threading

def main():
    n, m = map(int, stdin.readline().split())
    a = [0] + list(map(int, stdin.readline().split()))  # 1-based indexing
    gph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, stdin.readline().split())
        gph[x].append(y)
        gph[y].append(x)
    
    ans = 0

    def dfs(x, parent, cons_cats):
        nonlocal ans
        # Remove parent from adjacency list to avoid revisiting
        if parent in gph[x]:
            gph[x].remove(parent)
        
        if cons_cats > m:
            return
        
        # Check if current node is a leaf (no children left)
        if not gph[x]:
            ans += 1
            return
        
        for child in gph[x]:
            if a[child]:  # Child has a cat
                new_cons = cons_cats + 1
            else:
                new_cons = 0
            dfs(child, x, new_cons)
    
    dfs(1, 0, a[1])
    print(ans)

if __name__ == "__main__":
    threading.stack_size(1 << 27)
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()







arr = [int(i) for i in input().split()]