# Problem: Prime Pairs With Target Sum - https://leetcode.com/problems/prime-pairs-with-target-sum/description/

class Solution:
    def findPrimePairs(self,n):
        if n < 4:
            return [] 
        # do two sum on primes
        def prime_seive(n):
            is_prime,i = [True for _ in range(n+1)],2
            is_prime[0] = is_prime[1] = False
            
            while i *i <= n:
                if is_prime[i]:
                    j = i*i
                    for k in range(j,n+1,i):
                        is_prime[k] = False
                i += 1
            return is_prime

        prime_list = prime_seive(n)
        solution,seen = [],set()

        for i in range(2,n+1):
            if prime_list[i]:
                if (n-i) in seen:
                    if i < n-i:solution.append([i,n-i])
                    else:solution.append([n-i,i])
                seen.add(i)
    
        if n%2 == 0 and prime_list[n//2]:
            solution.append([n//2,n//2])
        if solution:
            solution.sort()

        return solution
                    