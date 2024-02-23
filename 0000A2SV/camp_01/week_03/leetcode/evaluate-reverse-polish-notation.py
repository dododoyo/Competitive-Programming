class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations,chars = {"+","-","*","/"}, []
        for token in tokens:
            if token in operations:
                a = chars.pop()
                b = chars.pop()
                # order of operation matters 
                if token == "+":solution = b + a
                elif token == "-":solution = b - a
                elif token == "*":solution = b * a
                elif token == "/":solution = int(b / a)
                chars.append(solution)
            else:
                chars.append(int(token))
        return chars[0]