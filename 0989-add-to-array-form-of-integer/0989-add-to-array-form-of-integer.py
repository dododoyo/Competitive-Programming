class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        carry = 0
        num_len = len(num)
        index = 0
        
        while k:
            least_k = k%10
                
            if index < num_len:
                num[index] += least_k
            else:
                num.append(least_k)
            
            carry = num[index] // 10
            num[index] = num[index] % 10
            
            k = k//10
            k += carry
            
            index += 1
            
        num.reverse()

        return num
                