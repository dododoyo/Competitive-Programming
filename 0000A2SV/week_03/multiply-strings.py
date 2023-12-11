class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        # reverse the nums for easier calculation
        reversed_num1,reversed_num2 = num1[::-1],num2[::-1]
        solution,carry = [0]*(len(num1)+len(num2)),0


        for i in range(len(num1)):
            for j in range(len(num2)):
                current_num = int(reversed_num1[i])*int(reversed_num2[j])
                result_num = current_num + solution[i+j]
                solution[i+j] = result_num%10
                solution[i+j+1] += result_num//10

        # reverse the solution 
        solution = solution[::-1]
        
        begining = 0
        # remove leading zeros
        while solution[begining] == 0:begining+=1
        
        return "".join(map(str,solution[begining:]))