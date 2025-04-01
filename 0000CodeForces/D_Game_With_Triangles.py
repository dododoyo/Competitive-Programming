from sys import stdin
def input(): return stdin.readline().strip()

for _ in range([int(i) for i in input().split()][0]):
    n, m = [int(i) for i in input().split()]
    top_points = sorted([int(i) for i in input().split()])
    bottom_points = sorted([int(i) for i in input().split()])

    # prefix_top[i] stores 
    # the sum of distances of *mirrored points*
    # from both ends in a line.

    prefix_top = [0] * (n//2 + 1)
    prefix_bottom = [0] * (m//2 + 1)
    solution = []

    for i in range(n//2):
        left_point,right_point = i,n-i-1
        curr_distance = top_points[right_point] - top_points[left_point]

        prefix_top[i + 1] = prefix_top[i] + curr_distance

    for i in range(m//2):
        left_point,right_point = i,m-i-1
        curr_distance = bottom_points[right_point] - bottom_points[left_point]

        prefix_bottom[i + 1] = prefix_bottom[i] + (curr_distance)

    # k => triangles

    for triangles in range(1, max(n, m)):
        # solves what will be the score if we take `top_triangles`
        # number of triangles from the top

        def score_of_k_top_triangles(top_triangles):
            bottom_triangles = triangles - top_triangles
            return prefix_top[top_triangles] + prefix_bottom[bottom_triangles]
        
        # Math 
        """
        lets suppose we wanted to make k number of triangles 

        let x be the number of triangles using the top as a base from the k triangles
        let k-x be the number of triangles using the bottom as a base

        ###############################################
        for base we will need 2*x points from top 
        and for the apex of the triangle that has base at bottom line 
        we need k-x points from top 
        
        in total we need x + x + k - x = x + k  
        so x+k <= n (we need atleast x+k points from top)
        in other words  x <= n - k
        ############################################
        
        if we make (k-x) points based on bottom 
        we need 2*(k-x) for the base and additional 
        x to be the apex for the top based triangles 

        2*(k-x) + x = k + k - x - x + x = 2*k - x
        so we need 2*k - x so 2k - x <= m  so 
        2k - m <= x => x >= 2k - m

        and it is natural to say 0 <= x <= k 
                        # """
        

        left, right = max(0, 2*triangles - m), min(triangles, n - triangles)

        if left > right:
            break
        
        valid = right
        
        # find valid boundaries for each move 
        while left < right:
            
            mid = left + (right-left) // 2
            not_last = mid + 1 <= right
            if not_last and score_of_k_top_triangles(mid) < score_of_k_top_triangles(mid + 1):
                left = mid + 1
            else:
                valid = mid
                right = mid
        
        # take the maximum from the valid moves
        solution.append(score_of_k_top_triangles(valid))

    print(len(solution))
    print(*solution)