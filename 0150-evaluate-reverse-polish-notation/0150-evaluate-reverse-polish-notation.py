class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in "*+-/":
                stk.append(int(i))
            else:
                num1,num2 = stk.pop(),stk.pop()
                if i == "*":stk.append(num1*num2);
                elif i == "+":stk.append(num1+num2);
                elif i == "-":stk.append(num2-num1)
                elif i == "/":stk.append(int(num2/num1))
        return stk[0]
        