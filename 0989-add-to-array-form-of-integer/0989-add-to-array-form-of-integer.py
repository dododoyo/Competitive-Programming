class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        carry = 0
        num_len = len(num)
        index = 0
        
        while k:
            #get the least index
            least_k = k%10
               
            # if index is within the number add it in position
            if index < num_len:
                num[index] += least_k
                
            # if solution may need more space than num?
            # append it to the end
            else:
                num.append(least_k)
            
            # get the carry element
            carry = num[index] // 10
            
            #update the index element with it's correct value
            num[index] = num[index] % 10
            
            #update k
            k = k//10
            
            #add carry element to k
            k += carry
            
            #increase the index of array
            index += 1
        
        #reverse the num
        num.reverse()

        return num
                