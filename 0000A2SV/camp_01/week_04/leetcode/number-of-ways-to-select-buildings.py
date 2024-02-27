class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        # at 0 we say how many 10s are after me 
        # at 1 we say how many 01s are after me 

        # get prefix sum of 10s after me 
        # get prefix sum of 01s after me

        int_s = [int(i) for i in s]
        
        one_count = int_s[:]
        zero_count = [int(not(i)) for i in int_s]

        one_prefix = [0]*n
        zero_prefix = [0]*n

        for i in range(1,n):
            one_prefix[n-i-1] = one_prefix[n-i] + one_count[n-i]
            zero_prefix[n-i-1] = zero_prefix[n-i] + zero_count[n-i] 
        
        zero_ones = [0]*n
        one_zeros = [0]*n

        for i in range(n-1):
            # print(zero_count[i])
            zero_ones[i] = zero_count[i]*one_prefix[i]
            one_zeros[i] = one_count[i]*zero_prefix[i]

        solution = 0

        for i in range(1,n):
            zero_ones[n-i-1] += zero_ones[n-i] 
            one_zeros[n-i-1] += one_zeros[n-i] 

        for i in range(n-2):
            if s[i] == "1":
                # ask how many 01's after it
                solution += zero_ones[i]
            else:
                # ask how many 10's after it
                solution += one_zeros[i]
        return solution