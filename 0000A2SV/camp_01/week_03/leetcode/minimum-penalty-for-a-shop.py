class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        """
        Count the number of N before index 
        and number of Y after index"""
        forward_count = [0]*(n+1)
        backward_count = [0]*(n+1)
        for i in range(n):
            forward_count[i+1] = int(customers[i] == "Y")
            backward_count[i+1] = int(customers[i] == "N")
            
        penality_till_now = [backward_count[0]]*(n+1)
        penality_after_now = [forward_count[-1]]*(n+1)

        # get prefix_sum of in reverse of the adding direction
        for i in range(n-1,-1,-1):
            penality_after_now[i] = penality_after_now[i+1] + forward_count[i]
        for i in range(1,n+1):
            penality_till_now[i] = penality_till_now[i-1] + backward_count[i]

        minimum_penality,index = float("inf"),0
        
        for i in range(n+1):
            if i == 0:
                current_penality = penality_after_now[i]
            elif i == n:
                current_penality = penality_till_now[i]
            else:
                current_penality = penality_till_now[i]+penality_after_now[i+1]

            if current_penality < minimum_penality:
                minimum_penality = current_penality
                index = i
        return index
        